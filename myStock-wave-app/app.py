
from h2o_wave import main, app, Q, ui, on, run_on, data
from typing import Optional, List
from database.models import Base, Recommend, NASDAQStockMetadata
from database.seed_helpers import seed_symbols_valid_metadata, seed_recommend_csv_data
from database.recommendation import get_top_n_most_recent_recommended_securities 
from database.chart import get_close_chart, get_sma_20_diff_chart, get_mavg_100_close_chart
from sqlalchemy import create_engine

TOP_N_RECOMMENDATIONS = 3

sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1:3306/nasdaq_stock', pool_recycle=3600, pool_size=50, max_overflow=50)
dbConnection    = sqlEngine.connect()

# Bind the engine to the Base class
Base.metadata.bind = sqlEngine

# Use for page cards that should be removed when navigating away.
# For pages that should be always present on screen use q.page[key] = ...
def add_card(q, name, card) -> None:
    q.client.cards.add(name)
    q.page[name] = card


# Remove all the cards related to navigation.
def clear_cards(q, ignore: Optional[List[str]] = []) -> None:
    if not q.client.cards:
        return

    for name in q.client.cards.copy():
        if name not in ignore:
            del q.page[name]
            q.client.cards.remove(name)

@on('#page1')
async def page1(q: Q):
    q.page['sidebar'].value = '#page1'
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    top_recommended_securities = get_top_n_most_recent_recommended_securities(sqlEngine, TOP_N_RECOMMENDATIONS)
    for index, recommended_security in enumerate(top_recommended_securities.values()):
        add_card(q, f'info{index}', ui.tall_info_card(box='horizontal', name="", title=f"{recommended_security.symbol}", caption=f"{recommended_security.security_name}", icon='SpeedHigh'))
    add_card(q, 'article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='600px'), title='How does magic work',
        image='https://images.pexels.com/photos/624015/pexels-photo-624015.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        content='''
Welcome to Stock Autobots, a Stock Recommender System to help you invest and buy and/or sell stock. Usually it takes time researching companies and industries to choose the right stocks. Even with funds, fund managers are prone to 
human error and human bias. Therefore, we are providing an AI personalized recommender system toward stock investing that will be tailored toward your industry domains of interest. Our goal is to encourage you to learn about stock 
investing. Hopefully, by making it easier to do stock investing with our recommender system, potentially more people come into retirement with multiple sources of retirement savings.
        '''
    ))


@on('#page2')
async def page2(q: Q):
    q.page['sidebar'].value = '#page2'
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).

    ticker_with_mavg_close_over_time = get_mavg_100_close_chart(sqlEngine)
    ticker_with_close_pred_over_time = get_close_chart(sqlEngine, TOP_N_RECOMMENDATIONS)
    ticker_with_macd_diff_over_time_pytorch = get_sma_20_diff_chart(sqlEngine, "pytorch", TOP_N_RECOMMENDATIONS)
    ticker_with_macd_diff_over_time_transformers = get_sma_20_diff_chart(sqlEngine, "transformers", TOP_N_RECOMMENDATIONS)
    print(ticker_with_close_pred_over_time.keys())
    ticker_with_close_pred_over_time_first_recommended = next(iter(ticker_with_close_pred_over_time.values()))
    ticker_with_macd_diff_pred_over_time_first_recommended_pytorch = next(iter(ticker_with_macd_diff_over_time_pytorch.values()))
    ticker_with_macd_diff_pred_over_time_first_recommended_transformers = next(iter(ticker_with_macd_diff_over_time_transformers.values()))

    add_card(q, 'mavg100_close_price', ui.plot_card(
        box='horizontal',
        title='Moving Average 100 Vs Close Price (GOOGL Ex)',
        data=data('days close_type price', len(ticker_with_mavg_close_over_time["GOOGL"]),
            rows=ticker_with_mavg_close_over_time["GOOGL"]
        ),
        plot=ui.plot([
            ui.mark(type='line', x='=days', y='=price', color='=close_type')
        ])
    ))
    add_card(q, 'close_price', ui.plot_card(
        box='horizontal',
        title='Close price over time',
        data=data('date price', len(ticker_with_close_pred_over_time_first_recommended), rows=ticker_with_close_pred_over_time_first_recommended),
        plot=ui.plot([ui.mark(type='line', x_scale='time', x='=date', y='=price', y_min=0)])
    ))
    add_card(q, 'pytorch_sma_20', ui.plot_card(
        box='horizontal',
        title='SMA 20 over time pytorch',
        data=data('date price', len(ticker_with_macd_diff_pred_over_time_first_recommended_pytorch), rows=ticker_with_macd_diff_pred_over_time_first_recommended_pytorch),
        plot=ui.plot([ui.mark(type='line', x_scale='time', x='=date', y='=price', y_min=0)])
    ))
    add_card(q, 'transformers_sma_20', ui.plot_card(
        box='horizontal',
        title='SMA 20 over time transformers',
        data=data('date price', len(ticker_with_macd_diff_pred_over_time_first_recommended_transformers), rows=ticker_with_macd_diff_pred_over_time_first_recommended_transformers),
        plot=ui.plot([ui.mark(type='line', x_scale='time', x='=date', y='=price', y_min=0)])
    ))

    # TODO: Either we have a download button for the graphs or we have this table where we can
    # download the data from our graphs listed in this table
    # add_card(q, 'table', ui.form_card(box='vertical', items=[ui.table(
    #     name='table',
    #     downloadable=True,
    #     resettable=True,
    #     groupable=True,
    #     columns=[
    #         ui.table_column(name='text', label='Process', searchable=True),
    #         ui.table_column(name='tag', label='Status', filterable=True, cell_type=ui.tag_table_cell_type(
    #             name='tags',
    #             tags=[
    #                 ui.tag(label='FAIL', color='$red'),
    #                 ui.tag(label='DONE', color='#D2E3F8', label_color='#053975'),
    #                 ui.tag(label='SUCCESS', color='$mint'),
    #             ]
    #         ))
    #     ],
    #     rows=[
    #         ui.table_row(name='row1', cells=['Process 1', 'FAIL']),
    #         ui.table_row(name='row2', cells=['Process 2', 'SUCCESS,DONE']),
    #         ui.table_row(name='row3', cells=['Process 3', 'DONE']),
    #         ui.table_row(name='row4', cells=['Process 4', 'FAIL']),
    #         ui.table_row(name='row5', cells=['Process 5', 'SUCCESS,DONE']),
    #         ui.table_row(name='row6', cells=['Process 6', 'DONE']),
    #     ])
    # ]))


@on('#page3')
async def page3(q: Q):
    q.page['sidebar'].value = '#page3'
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).

    for i in range(12):
        add_card(q, f'item{i}', ui.wide_info_card(box=ui.box('grid', width='400px'), name='', title='Tile',
                                                  caption='Lorem ipsum dolor sit amet'))


@on('#page4')
@on('page4_reset')
async def page4(q: Q):
    q.page['sidebar'].value = '#page4'
    # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    # Since this page is interactive, we want to update its card
    # instead of recreating it every time, so ignore 'form' card on drop.
    clear_cards(q, ['form'])

    # If first time on this page, create the card.
    add_card(q, 'form', ui.form_card(box='vertical', items=[
        ui.stepper(name='stepper', items=[
            ui.step(label='Step 1'),
            ui.step(label='Step 2'),
            ui.step(label='Step 3'),
        ]),
        ui.textbox(name='textbox1', label='Textbox 1'),
        ui.buttons(justify='end', items=[
            ui.button(name='page4_step2', label='Next', primary=True),
        ]),
    ]))


@on()
async def page4_step2(q: Q):
    # Just update the existing card, do not recreate.
    q.page['form'].items = [
        ui.stepper(name='stepper', items=[
            ui.step(label='Step 1', done=True),
            ui.step(label='Step 2'),
            ui.step(label='Step 3'),
        ]),
        ui.textbox(name='textbox2', label='Textbox 2'),
        ui.buttons(justify='end', items=[
            ui.button(name='page4_step3', label='Next', primary=True),
        ])
    ]


@on()
async def page4_step3(q: Q):
    # Just update the existing card, do not recreate.
    q.page['form'].items = [
        ui.stepper(name='stepper', items=[
            ui.step(label='Step 1', done=True),
            ui.step(label='Step 2', done=True),
            ui.step(label='Step 3'),
        ]),
        ui.textbox(name='textbox3', label='Textbox 3'),
        ui.buttons(justify='end', items=[
            ui.button(name='page4_reset', label='Finish', primary=True),
        ])
    ]


async def init(q: Q) -> None:
    q.page['meta'] = ui.meta_card(box='', layouts=[ui.layout(breakpoint='xs', min_height='100vh', zones=[
        ui.zone('main', size='1', direction=ui.ZoneDirection.ROW, zones=[
            ui.zone('sidebar', size='250px'),
            ui.zone('body', zones=[
                ui.zone('header'),
                ui.zone('content', zones=[
                    # Specify various zones and use the one that is currently needed. Empty zones are ignored.
                    ui.zone('horizontal', direction=ui.ZoneDirection.ROW),
                    ui.zone('vertical'),
                    ui.zone('grid', direction=ui.ZoneDirection.ROW, wrap='stretch', justify='center')
                ]),
            ]),
        ])
    ])])
    sjsu_logo_url = "https://raw.githubusercontent.com/Financial-AI/Stock-Recommender-System/main/images/San_Jose_State_Spartans_logo.png"

    q.page['sidebar'] = ui.nav_card(
        box='sidebar', color='primary', title='Stock Autobots', subtitle="Stock Recommender System",
        value=f'#{q.args["#"]}' if q.args['#'] else '#page1',
        image=sjsu_logo_url, items=[
            ui.nav_group('Menu', items=[
                ui.nav_item(name='#page1', label='Home'),
                ui.nav_item(name='#page2', label='EDA Telemetry'),
                ui.nav_item(name='#page3', label='Train Model'),
                ui.nav_item(name='#page4', label='Deploy Model'),
            ]),
        ])
    q.page['header'] = ui.header_card(
        box='header', title='', subtitle='',
        secondary_items=[ui.textbox(name='search', icon='Search', width='400px', placeholder='Search...')],
        items=[
            ui.persona(title='Juan Gomez', subtitle='Developer', size='xs',
                       image='https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&h=750&w=1260'),
        ]
    )
    # If no active hash present, render page1.
    if q.args['#'] is None:
        await page1(q)


@app('/')
async def serve(q: Q):
    # Run only once per client connection.
    if not q.client.initialized:
        q.client.cards = set()
        await init(q)
        q.client.initialized = True

    # Handle routing.
    await run_on(q)
    await q.page.save()

