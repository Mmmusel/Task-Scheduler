# 各种图的html

# 登录页面icon
def goto_creat_icon_html():
    the_html_content = '''
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 50%">
        <head>
          <meta charset="utf-8">
        </head>
        <body style="height: 100%; margin: 0">
          <div id="container" style="height: 100%"></div>

          <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.3.3/dist/echarts.min.js"></script>
          <script type="text/javascript">
            var dom = document.getElementById('container');
            var myChart = echarts.init(dom, null, {
              renderer: 'canvas',
              useDirtyRect: false,
            });
            var app = {};
            var option;
        
            option = {
        graphic: {

            elements: [
              {
                type: 'text',
                left: 'center',
                top: 'center',
                style: {
                  text: 'LLL',
                  fontSize: 50,
                  fontWeight: 'bold',
                  lineDash: [0, 200],
                  lineDashOffset: 0,
                  fill: 'transparent',
                  stroke: '#000',
                  lineWidth: 1
                },
                keyframeAnimation: {           
                  duration: 3000,
                  loop: true,
                  keyframes: [
                    {
                      percent: 0.5,
                      style: {
                        fill: 'transparent',
                        lineDashOffset: 200,
                        lineDash: [200, 0]
                      }
                    },
                    {
                      // Stop for a while.
                      percent: 1.8,
                      style: {
                        fill: 'transparent'
                      }
                    },
                    {
                      percent: 1,
                      style: {
                        fill: 'black'
                      }
                    }
                  ]
                }
              }
            ]
          }
        };
        
            if (option && typeof option === 'object') {
              myChart.setOption(option);
            }
            window.addEventListener('resize', myChart.resize);
          </script>
        </body>
        </html>
    '''

    return the_html_content


# 仅含文本content的html
def goto_creat_empty_html(content):
    the_html_content = '''
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 50%">
        <head>
            <meta charset="utf-8">
        </head>
        <body style="height: 100%; margin: 0">
            <div id="container" style="height: 100%"></div>
        <h2 align = "center">'''
    the_html_content = the_html_content + content + "</h2>"
    the_html_content = the_html_content + '''
                                            </body>
                                            </html>'''
    return the_html_content


# 创建[每日]类别时间分配饼状图
def goto_creat_daypie_html(day, day_dic):
    the_html_content = '''
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 50%">
        <head>
            <meta charset="utf-8">
        </head>
        <body style="height: 100%; margin: 0">
            <div id="container" style="height: 100%"></div>

        <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
        <script type="text/javascript">
            var dom = document.getElementById("container");
            var myChart = echarts.init(dom, null, {
                renderer: 'canvas',
                useDirtyRect: false
            });
            var app = {};
            var option;
            option = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                title: {
                    text:'''

    the_html_content = the_html_content + "'" + day + "时间分配(单位:分钟)" + "',"
    the_html_content = the_html_content + '''left: 'left'
                                            },
                                            legend: {
                                                orient: 'vertical',
                                                left: 'right',
                                            },'''

    the_html_content = the_html_content + '''series: ['''

    the_html_content = the_html_content + '''{
                                                name: '单日时间分配',
                                                type: 'pie',
                                                radius:'70%',
                                                emphasis: {
                                                    itemStyle: {
                                                        shadowBlur: 10,
                                                        shadowOffsetX: 0,
                                                        shadowColor: 'rgba(0, 0, 0, 0.5)'}
                                                    },
                                                data:['''
    for key, value in day_dic.items():
        the_html_content = the_html_content + "{ value:" + str(value) \
                           + ", name: '" + key + "'},"
    the_html_content = the_html_content + "]},"

    the_html_content = the_html_content + ''']};
            if (option && typeof option === 'object') {myChart.setOption(option);}
            window.addEventListener('resize', myChart.resize);
        </script>
    </body>
    </html>
    '''
    return the_html_content


# 创建[每周]类别时间分配饼状图+折线图
def goto_creat_week_pie_line_html(date_list, data):
    the_html_content = '''
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 100%">
        <head>
            <meta charset="utf-8">
        </head>
        <body style="height: 100%; margin: 0">
            <div id="container" style="height: 100%"></div>
    
            <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
            <script type="text/javascript">
                var dom = document.getElementById('container');
                var myChart = echarts.init(dom, null, {
                  renderer: 'canvas',
                  useDirtyRect: false
                });
                var app = {};
        
                var option;
    
                setTimeout(function () {
              option = {
                legend: {},
                tooltip: {
                  trigger: 'axis',
                  showContent: true
                },
                dataset: {
                  source: ['''
    date_list.insert(0, 'product')
    the_html_content = the_html_content + str(date_list)

    # 汇总数据
    cates = set()  # 所有的类别
    for dic in data:  # data里含有7个字典
        for key in dic.keys():  # key为类别
            cates.add(key)

    all_data = dict()  # key为类别，value为含有7个元素的列表

    for cate in cates:  # 遍历所有类别
        tmp = []
        for dic in data:  # data里含有7个字典
            if cate in dic:
                tmp.append(dic[cate])
            else:
                tmp.append(0)
        all_data[cate] = tmp

    for key, value in all_data.items():  # key为类别，value为含有7个元素的列表
        tmp_list = value
        tmp_list.insert(0, key)
        the_html_content = the_html_content + "," + str(tmp_list)
    the_html_content = the_html_content + "]},"

    the_html_content = the_html_content + '''xAxis: { type: 'category' },
                                            yAxis: { gridIndex: 0 },
                                            grid: { top: '55%' },
                                            series: ['''

    for i in range(len(all_data)):
        the_html_content = the_html_content + '''{
                                                    type: 'line',
                                                    smooth: false,
                                                    seriesLayoutBy: 'row',
                                                    emphasis: { focus: 'series' }
                                                  },'''

    the_html_content = the_html_content + '''                
            {
                type: 'pie',
                id: 'pie',
                radius: '30%',
                center: ['50%', '25%'],
                emphasis: {
                    focus: 'self'
                },
                label: {
                    formatter: '{b}: {@2012} ({d}%)'
                },
                encode: {
                    itemName: 'product',
                    value: '2012',
                    tooltip: '2012'
                }
            }
        ]
    };
    myChart.on('updateAxisPointer', function (event) {
        const xAxisInfo = event.axesInfo[0];
        if (xAxisInfo) {
            const dimension = xAxisInfo.value + 1;
            myChart.setOption({
                series: {
                  id: 'pie',
                  label: {
                    formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                  },
                  encode: {
                    value: dimension,
                    tooltip: dimension
                  }
                }
              });
            }
          });
          myChart.setOption(option);
        });
        
            if (option && typeof option === 'object') {
              myChart.setOption(option);
            }
        
            window.addEventListener('resize', myChart.resize);
          </script>
        </body>
        </html>'''
    return the_html_content


# 创建[每月]类别时间分配柱状图
def goto_creat_month_bar_html(date_list, data):
    the_html_content = '''
        <!DOCTYPE html>
        <html lang="zh-CN" style="height: 100%">
        <head>
            <meta charset="utf-8">
        </head>
        <body style="height: 100%; margin: 0">
            <div id="container" style="height: 100%"></div>
        
        <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.3.3/dist/echarts.min.js"></script>
        <script type="text/javascript">
            var dom = document.getElementById('container');
            var myChart = echarts.init(dom, null, {
                renderer: 'canvas',
                useDirtyRect: false
            });
            var app = {};
    
            var option;
        '''

    # 汇总数据
    cates = set()  # 所有的类别
    for dic in data:  # data里含有n个字典，n为该月天数
        for key in dic.keys():  # key为类别
            cates.add(key)

    all_data = dict()  # key为类别，value为含有n个元素的列表

    for cate in cates:  # 遍历所有类别
        tmp = []
        for dic in data:  # data里含有n个字典
            if cate in dic:
                tmp.append(dic[cate])
            else:
                tmp.append(0)
        all_data[cate] = tmp

    # 设置xAxisData
    the_html_content = the_html_content + "let xAxisData = ["
    for i in range(1, len(date_list) + 1):
        if i == 1:
            the_html_content = the_html_content + str(i)
        else:
            the_html_content = the_html_content + ", " + str(i)
    the_html_content = the_html_content + "];"

    the_html_content = the_html_content + '''var emphasisStyle = {
                                                itemStyle: {
                                                    shadowBlur: 10,
                                                    shadowColor: 'rgba(0,0,0,0.3)'
                                                }
                                            };
                                            option = {
                                                legend: {
                                                data: ['''
    i = 1
    for key, value in all_data.items():
        if i == 1:
            the_html_content = the_html_content + "'" + str(key) + "'"
        else:
            the_html_content = the_html_content + ", '" + str(key) + "'"
        i += 1
    the_html_content = the_html_content + "],"

    the_html_content = the_html_content + '''
        left: '10%'
        },
        toolbox: {
            feature: {
                magicType: {
                    type: ['stack']
                },
              dataView: {}
            }
        },
        tooltip: {},
        xAxis: {
            data: xAxisData,
            name: '日期',
            axisLine: { onZero: true },
            splitLine: { show: false },
            splitArea: { show: false }
        },
        yAxis: {},
        grid: {
            bottom: 100
        },
        series: ['''

    i = 1
    for key, value in all_data.items():
        if i == 1:
            the_html_content = the_html_content + "{name: '" + str(key) + "',"\
                               + '''type: 'bar',
                                    stack: 'one',
                                    emphasis: emphasisStyle,
                                    data: ''' + str(value) + "}"
        else:
            the_html_content = the_html_content + ",{name: '" + str(key) + "'," \
                               + '''type: 'bar',
                                    stack: 'one',
                                    emphasis: emphasisStyle,
                                    data: ''' + str(value) + "}"
        i += 1
    the_html_content = the_html_content + "]};"

    the_html_content = the_html_content + '''
        myChart.on('brushSelected', function () {
            
        myChart.setOption({
            title: {
                backgroundColor: '#333',
                text: 'SELECTED DATA INDICES: \\n' + brushed.join('\\n'),
                bottom: 0,
                right: '10%',
                width: 100,
                textStyle: {
                    fontSize: 12,
                    color: '#fff'
                }
            }
        });
    });

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
  </script>
</body>
</html>
    '''

    return the_html_content
