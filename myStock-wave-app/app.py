
from h2o_wave import main, app, Q, ui, on, run_on, data
from typing import Optional, List
from database.models import Base, Recommend, NASDAQStockMetadata
from database.seed_helpers import seed_symbols_valid_metadata, seed_recommend_csv_data
from database.recommendation import get_top_n_most_recent_recommended_securities
from sqlalchemy import create_engine

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
    top_recommended_securities = get_top_n_most_recent_recommended_securities(sqlEngine, 2)
    for index, recommended_security in enumerate(top_recommended_securities):
        add_card(q, f'info{index}', ui.tall_info_card(box='horizontal', name="", title=f"{recommended_security.symbol}", caption=f"{recommended_security.security_name}", icon='SpeedHigh'))
    # add_card(q, 'chart1', ui.plot_card(
    #     box='horizontal',
    #     title='Chart 1',
    #     data=data('category country product price', 10, rows=[
    #         ('G1', 'USA', 'P1', 124),
    #         ('G1', 'China', 'P2', 580),
    #         ('G1', 'USA', 'P3', 528),
    #         ('G1', 'China', 'P1', 361),
    #         ('G1', 'USA', 'P2', 228),
    #         ('G2', 'China', 'P3', 418),
    #         ('G2', 'USA', 'P1', 824),
    #         ('G2', 'China', 'P2', 539),
    #         ('G2', 'USA', 'P3', 712),
    #         ('G2', 'USA', 'P1', 213),
    #     ]),
    #     plot=ui.plot([ui.mark(type='interval', x='=product', y='=price', color='=country', stack='auto',
    #                           dodge='=category', y_min=0)])
    # ))
    # add_card(q, 'chart2', ui.plot_card(
    #     box='horizontal',
    #     title='Chart 2',
    #     data=data('date price', 10, rows=[
    #         ('2020-03-20', 124),
    #         ('2020-05-18', 580),
    #         ('2020-08-24', 528),
    #         ('2020-02-12', 361),
    #         ('2020-03-11', 228),
    #         ('2020-09-26', 418),
    #         ('2020-11-12', 824),
    #         ('2020-12-21', 539),
    #         ('2020-03-18', 712),
    #         ('2020-07-11', 213),
    #     ]),
    #     plot=ui.plot([ui.mark(type='line', x_scale='time', x='=date', y='=price', y_min=0)])
    # ))
    add_card(q, 'article', ui.tall_article_preview_card(
        box=ui.box('vertical', height='600px'), title='How does magic work',
        image='https://images.pexels.com/photos/624015/pexels-photo-624015.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        content='''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac sodales felis. Duis orci enim, iaculis at augue vel, mattis imperdiet ligula. Sed a placerat lacus, vitae viverra ante. Duis laoreet purus sit amet orci lacinia, non facilisis ipsum venenatis. Duis bibendum malesuada urna. Praesent vehicula tempor volutpat. In sem augue, blandit a tempus sit amet, tristique vehicula nisl. Duis molestie vel nisl a blandit. Nunc mollis ullamcorper elementum.
Donec in erat augue. Nullam mollis ligula nec massa semper, laoreet pellentesque nulla ullamcorper. In ante ex, tristique et mollis id, facilisis non metus. Aliquam neque eros, semper id finibus eu, pellentesque ac magna. Aliquam convallis eros ut erat mollis, sit amet scelerisque ex pretium. Nulla sodales lacus a tellus molestie blandit. Praesent molestie elit viverra, congue purus vel, cursus sem. Donec malesuada libero ut nulla bibendum, in condimentum massa pretium. Aliquam erat volutpat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer vel tincidunt purus, congue suscipit neque. Fusce eget lacus nibh. Sed vestibulum neque id erat accumsan, a faucibus leo malesuada. Curabitur varius ligula a velit aliquet tincidunt. Donec vehicula ligula sit amet nunc tempus, non fermentum odio rhoncus.
Vestibulum condimentum consectetur aliquet. Phasellus mollis at nulla vel blandit. Praesent at ligula nulla. Curabitur enim tellus, congue id tempor at, malesuada sed augue. Nulla in justo in libero condimentum euismod. Integer aliquet, velit id convallis maximus, nisl dui porta velit, et pellentesque ligula lorem non nunc. Sed tincidunt purus non elit ultrices egestas quis eu mauris. Sed molestie vulputate enim, a vehicula nibh pulvinar sit amet. Nullam auctor sapien est, et aliquet dui congue ornare. Donec pulvinar scelerisque justo, nec scelerisque velit maximus eget. Ut ac lectus velit. Pellentesque bibendum ex sit amet cursus commodo. Fusce congue metus at elementum ultricies. Suspendisse non rhoncus risus. In hac habitasse platea dictumst.
        '''
    ))


@on('#page2')
async def page2(q: Q):
    q.page['sidebar'].value = '#page2'
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    add_card(q, 'chart1', ui.plot_card(
        box='horizontal',
        title='100 Moving Average Vs Close Price',
        data=data('category country product price', 10, rows=[
            ('G1', 'USA', 'P1', 124),
            ('G1', 'China', 'P2', 580),
            ('G1', 'USA', 'P3', 528),
            ('G1', 'China', 'P1', 361),
            ('G1', 'USA', 'P2', 228),
            ('G2', 'China', 'P3', 418),
            ('G2', 'USA', 'P1', 824),
            ('G2', 'China', 'P2', 539),
            ('G2', 'USA', 'P3', 712),
            ('G2', 'USA', 'P1', 213),
        ]),
        plot=ui.plot([ui.mark(type='interval', x='=product', y='=price', color='=country', stack='auto',
                              dodge='=category', y_min=0)])
    ))
    add_card(q, 'chart2', ui.plot_card(
        box='horizontal',
        title='Chart 2',
        data=data('date price', 10, rows=[
            ('2020-03-20', 124),
            ('2020-05-18', 580),
            ('2020-08-24', 528),
            ('2020-02-12', 361),
            ('2020-03-11', 228),
            ('2020-09-26', 418),
            ('2020-11-12', 824),
            ('2020-12-21', 539),
            ('2020-03-18', 712),
            ('2020-07-11', 213),
        ]),
        plot=ui.plot([ui.mark(type='line', x_scale='time', x='=date', y='=price', y_min=0)])
    ))
    add_card(q, 'table', ui.form_card(box='vertical', items=[ui.table(
        name='table',
        downloadable=True,
        resettable=True,
        groupable=True,
        columns=[
            ui.table_column(name='text', label='Process', searchable=True),
            ui.table_column(name='tag', label='Status', filterable=True, cell_type=ui.tag_table_cell_type(
                name='tags',
                tags=[
                    ui.tag(label='FAIL', color='$red'),
                    ui.tag(label='DONE', color='#D2E3F8', label_color='#053975'),
                    ui.tag(label='SUCCESS', color='$mint'),
                ]
            ))
        ],
        rows=[
            ui.table_row(name='row1', cells=['Process 1', 'FAIL']),
            ui.table_row(name='row2', cells=['Process 2', 'SUCCESS,DONE']),
            ui.table_row(name='row3', cells=['Process 3', 'DONE']),
            ui.table_row(name='row4', cells=['Process 4', 'FAIL']),
            ui.table_row(name='row5', cells=['Process 5', 'SUCCESS,DONE']),
            ui.table_row(name='row6', cells=['Process 6', 'DONE']),
        ])
    ]))


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
            ui.persona(title='John Doe', subtitle='Developer', size='xs',
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

