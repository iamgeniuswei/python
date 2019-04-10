from pyecharts import GeoLines, Style, Map

style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="circle",
    geo_effect_symbolsize=5,
    # label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
)

data_guangzhou = [
    ["北京", "南京"],
    ["北京", "沈阳"],
    ["北京", "合肥"],
    ["北京", "成都"],
    ["北京", "广州"],
    ["北京", "西安"],
    ["北京", "兰州"],
    ["北京", "乌鲁木齐"]
]
# map.render()

geolines = GeoLines("", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.render()