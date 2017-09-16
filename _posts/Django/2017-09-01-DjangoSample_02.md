---
layout: post
title: DjangoSample-02-应用ACE模板(html/css/javascript)-01
date: 2017-09-01 22:45:59
categories: Django
tags: Django总结
---
* content
{:toc}

> [DjangoSample-XX...]系列,记录平常做的一些Django范例程序。
> 作为自己以后工作时的参考信息。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 实现功能
1. 将ACE模板引入Django，并使用base.html，保持以后页面的可扩展，以及风格的统一。
2. 建立model，生成数据库表。
3. 在左边nav栏，从数据库读取层级数据，并动态加载显示。
4. 点击左边的nav栏，右边的pagecontent中显示对应的table。


# <i class="fa fa-cubes" style="font-size:1em;"></i> 1. 建立程序结构-app

- 创建project

```
C:\Users\61041150\djangoproject>myvenv\scripts\activate

(myvenv) C:\Users\61041150\djangoproject>django-admin startproject cmdbtool

(myvenv) C:\Users\61041150\djangoproject>
```

- 配置project

修改配置,将TIME_ZONE修改为「ASIA/TOKYO」,并追加设定static文件。

```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')#← 一行を追加
```

- 启动服务`python manage.py runserver`后，并访问`http://localhost:8000/`，可以看到如下的页面

```
It worked!
Congratulations on your first Django-powered page.
```

- 创建app，`python manage.py startapp zonemana`

- 修改setting，追加app

```
settings.py
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zonemana',
)
```

# <i class="fa fa-cubes" style="font-size:1em;"></i> 2. url/视图/模板

- 添加URL解析(project)

```
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('zonemana.urls')),
]
```

- 添加URL解析(app)

```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.query, name='query'),
]
```


- 添加视图

```
from django.shortcuts import render

# Create your views here.
def query(request):
    return render(request, 'zonemana/query.html', {})
```

- 创建`zonemana/templates/zonemana/query.html`模板

- 到上面为止，通过访问localhost可以进入上面的html页面。

# <i class="fa fa-cubes" style="font-size:1em;"></i> 3. 建立页面的模板结构

- 创建`base.html` `header.html` `leftnavi.html` `footer.html`

base.html中包含通用页面

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>[% block title %}構成管理[% endblock %}</title>
</head>
<body>
[% include 'zonemana\header.html'%}

[% include 'zonemana\leftnavi.html'%}

[% block content %}
 <div> 这里是默认部分，如果不覆盖就显示这里的默认内容</div>
[% endblock %}

[% include 'zonemana\footer.html'%}

</body>
</html>

```

- 将 query.html修改为

```python
[% extends 'zonemana\base.html' %}
[% block title %} 欢迎光临首页 [% endblock %}

[% block content %}

<h1>这里是首页，欢迎光临</h1>

[% endblock %}

```

最终显示如下:


![image](https://user-images.githubusercontent.com/18595935/30168847-8f1bd1ea-9425-11e7-931f-765cea2d6d61.png)


# <i class="fa fa-cubes" style="font-size:1em;"></i>  4. 引入ACE模板
通过上述过程，将框架搭建完毕后，下一步是引入ACE模板，并只保留自己需要的部分。

## 3.1 导入文件
在 app 的 zonemana 目录下新建文件夹 static，将ACE示例中的assets文件夹复制到这里来。
其目录构造不要修改

## 3.2  在setting中添加 如下

```python
STATICFILES_DIRS = (
  os.path.join(STATIC_ROOT, 'static/'),
)

```


## 3.3 修改相关html文件
当前包含 base.html,footer.html,header.html,leftnavi.html,query.html,queryscripts.html

### 1. base.html

```python
[% load staticfiles %}

<html lang="en">
    <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta charset="utf-8" />
    <title>[% block title %}構成管理[% endblock %}</title>

    <meta name="description" content="Static &amp; Dynamic Tables" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />

    <!-- bootstrap & fontawesome -->
    <link rel="stylesheet" href="[%static 'assets/css/bootstrap.min.css'%}"/>
    <link rel="stylesheet" href="[%static 'assets/font-awesome/4.5.0/css/font-awesome.min.css'%}"/>

    <!-- page specific plugin styles -->
    <link rel="stylesheet" href="[%static 'assets/css/jquery-ui.min.css'%}" />
    <link rel="stylesheet" href="[%static 'assets/css/bootstrap-datepicker3.min.css'%}" />
    <link rel="stylesheet" href="[%static 'assets/css/ui.jqgrid.min.css'%}" />

    <!-- text fonts -->
    <link rel="stylesheet" href="[%static 'assets/css/fonts.googleapis.com.css'%}"/>

    <!-- ace styles -->
    <link rel="stylesheet" href="[%static 'assets/css/ace.min.css'%}" class="ace-main-stylesheet" id="main-ace-style" />

    <!--[if lte IE 9]>
    <link rel="stylesheet" href="[%static 'assets/css/ace-part2.min.css'%}" class="ace-main-stylesheet" />
    <![endif]-->
    <link rel="stylesheet" href="[%static 'assets/css/ace-skins.min.css'%}"/>
    <link rel="stylesheet" href="[%static 'assets/css/ace-rtl.min.css'%}"/>

    <!--[if lte IE 9]>
    <link rel="stylesheet" href="[%static 'assets/css/ace-ie.min.css'%}"/>
    <![endif]-->

    <!-- inline styles related to this page -->

    <!-- ace settings handler -->
    <script src="[%static 'assets/js/ace-extra.min.js'%}"></script>

    <!-- HTML5shiv and Respond.js for IE8 to support HTML5 elements and media queries -->

    <!--[if lte IE 8]>
    <script src="[%static 'assets/js/html5shiv.min.js'%}"></script>
    <script src="[%static 'assets/js/respond.min.js'%}"></script>
    <![endif]-->
</head>
    <body class="no-skin">
        [% include 'zonemana\header.html'%}

        <div class="main-container ace-save-state" id="main-container">
            [% include 'zonemana\leftnavi.html'%}

            [% block content %}
                <div> content 默认部分，如果不覆盖就显示这里的默认内容</div>
            [% endblock %}

            [% include 'zonemana\footer.html'%}
        </div><!-- /.main-container -->

        [% block queryScript%}
            <div>scripts 默认部分，如果不覆盖就显示这里的默认内容</div>
        [% endblock %}
    </body>
</html>

```

### 2. footer.html

```python

<div class="footer">
	<div class="footer-inner">
		<div class="footer-content">
			<span class="bigger-120">
				<span class="blue bolder">IDCF</span>
				Application
			</span>
		</div>
	</div>
</div>

<a href="#" id="btn-scroll-up" class="btn-scroll-up btn btn-sm btn-inverse">
	<i class="ace-icon fa fa-angle-double-up icon-only bigger-110"></i>
</a>

```

### 3.  header.html

```python
<div id="navbar" class="navbar navbar-default          ace-save-state">
	<div class="navbar-header pull-left">
					<a href="/" class="navbar-brand">
						<small>
							<i class="fa fa-cloud" aria-hidden="true">Zone構成管理</i>
						</small>
					</a>
	</div>
</div>
```


### 4. leftnavi.html

```python

<div id="sidebar" class="sidebar responsive    ace-save-state">
	<script type="text/javascript">
		try{ace.settings.loadState('sidebar')}catch(e){}
	</script>
	<ul class="nav nav-list">
		<li class="active open">
			<a href="#" class="dropdown-toggle">
				<i class="menu-icon fa fa-list"></i>
				<span class="menu-text"> Tables </span>
				<b class="arrow fa fa-angle-down"></b>
			</a>
			<b class="arrow"></b>
			<ul class="submenu">
				<li class="active">
					<a href="tables.html">
						<i class="menu-icon fa fa-caret-right"></i>
						Simple &amp; Dynamic
					</a>
					<b class="arrow"></b>
				</li>
				<li class="">
					<a href="jqgrid.html">
						<i class="menu-icon fa fa-caret-right"></i>
						jqGrid plugin
					</a>
					<b class="arrow"></b>
				</li>
			</ul>
		</li>
	</ul><!-- /.nav-list -->

	<div class="sidebar-toggle sidebar-collapse" id="sidebar-collapse">
		<i id="sidebar-toggle-icon" class="ace-icon fa fa-angle-double-left ace-save-state" data-icon1="ace-icon fa fa-angle-double-left" data-icon2="ace-icon fa fa-angle-double-right"></i>
	</div>
</div>
```


### 5. query.html 查询主页面

```python
<div id="sidebar" class="sidebar responsive    ace-save-state">
	<script type="text/javascript">
		try{ace.settings.loadState('sidebar')}catch(e){}
	</script>
	<ul class="nav nav-list">
		<li class="active open">
			<a href="#" class="dropdown-toggle">
				<i class="menu-icon fa fa-list"></i>
				<span class="menu-text"> Tables </span>
				<b class="arrow fa fa-angle-down"></b>
			</a>
			<b class="arrow"></b>
			<ul class="submenu">
				<li class="active">
					<a href="tables.html">
						<i class="menu-icon fa fa-caret-right"></i>
						Simple &amp; Dynamic
					</a>
					<b class="arrow"></b>
				</li>
				<li class="">
					<a href="jqgrid.html">
						<i class="menu-icon fa fa-caret-right"></i>
						jqGrid plugin
					</a>
					<b class="arrow"></b>
				</li>
			</ul>
		</li>
	</ul><!-- /.nav-list -->

	<div class="sidebar-toggle sidebar-collapse" id="sidebar-collapse">
		<i id="sidebar-toggle-icon" class="ace-icon fa fa-angle-double-left ace-save-state" data-icon1="ace-icon fa fa-angle-double-left" data-icon2="ace-icon fa fa-angle-double-right"></i>
	</div>
</div>

```

### 6.  queryscripts.html

```python

[% load staticfiles %}

<!-- basic scripts -->

<!--[if !IE]> -->
<script src="[%static 'assets/js/jquery-2.1.4.min.js'%}"></script>
<!-- <![endif]-->

<!--[if IE]>
<script src="[%static 'assets/js/jquery-1.11.3.min.js'%}"></script>
<![endif]-->

<script type="text/javascript">
	if('ontouchstart' in document.documentElement) document.write("<script src='[%static 'assets/js/jquery.mobile.custom.min.js'%}'>"+"<"+"/script>");
</script>
<script src="[%static 'assets/js/bootstrap.min.js'%}"></script>

<!-- page specific plugin scripts -->
<script src="[%static 'assets/js/jquery.dataTables.min.js'%}"></script>
<script src="[%static 'assets/js/jquery.dataTables.bootstrap.min.js'%}"></script>
<script src="[%static 'assets/js/dataTables.buttons.min.js'%}"></script>
<script src="[%static 'assets/js/buttons.flash.min.js'%}"></script>
<script src="[%static 'assets/js/buttons.html5.min.js'%}"></script>
<script src="[%static 'assets/js/buttons.print.min.js'%}"></script>
<script src="[%static 'assets/js/buttons.colVis.min.js'%}"></script>
<script src="[%static 'assets/js/dataTables.select.min.js'%}"></script>

<!-- ace scripts -->
<script src="[%static 'assets/js/ace-elements.min.js'%}"></script>
<script src="[%static 'assets/js/ace.min.js'%}"></script>

<!-- inline scripts related to this page -->
<script type="text/javascript">
jQuery(function($) {
	//initiate dataTables plugin
	var myTable =
	$('#dynamic-table')
	//.wrap("<div class='dataTables_borderWrap' />")   //if you are applying horizontal scrolling (sScrollX)
	.DataTable( {
		bAutoWidth: false,
		"aoColumns": [
		  { "bSortable": false },
		  null, null,null, null, null,
		  { "bSortable": false }
		],
		"aaSorting": [],


		//"bProcessing": true,
        //"bServerSide": true,
        //"sAjaxSource": "http://127.0.0.1/table.php"	,

		//,
		//"sScrollY": "200px",
		//"bPaginate": false,

		//"sScrollX": "100%",
		//"sScrollXInner": "120%",
		//"bScrollCollapse": true,
		//Note: if you are applying horizontal scrolling (sScrollX) on a ".table-bordered"
		//you may want to wrap the table inside a "div.dataTables_borderWrap" element

		//"iDisplayLength": 50


		select: {
			style: 'multi'
		}
    } );



	$.fn.dataTable.Buttons.defaults.dom.container.className = 'dt-buttons btn-overlap btn-group btn-overlap';

	new $.fn.dataTable.Buttons( myTable, {
		buttons: [
		  {
			"extend": "colvis",
			"text": "<i class='fa fa-search bigger-110 blue'></i> <span class='hidden'>Show/hide columns</span>",
			"className": "btn btn-white btn-primary btn-bold",
			columns: ':not(:first):not(:last)'
		  },
		  {
			"extend": "copy",
			"text": "<i class='fa fa-copy bigger-110 pink'></i> <span class='hidden'>Copy to clipboard</span>",
			"className": "btn btn-white btn-primary btn-bold"
		  },
		  {
			"extend": "csv",
			"text": "<i class='fa fa-database bigger-110 orange'></i> <span class='hidden'>Export to CSV</span>",
			"className": "btn btn-white btn-primary btn-bold"
		  },
		  {
			"extend": "excel",
			"text": "<i class='fa fa-file-excel-o bigger-110 green'></i> <span class='hidden'>Export to Excel</span>",
			"className": "btn btn-white btn-primary btn-bold"
		  },
		  {
			"extend": "pdf",
			"text": "<i class='fa fa-file-pdf-o bigger-110 red'></i> <span class='hidden'>Export to PDF</span>",
			"className": "btn btn-white btn-primary btn-bold"
		  },
		  {
			"extend": "print",
			"text": "<i class='fa fa-print bigger-110 grey'></i> <span class='hidden'>Print</span>",
			"className": "btn btn-white btn-primary btn-bold",
			autoPrint: false,
			message: 'This print was produced using the Print button for DataTables'
		  }
		]
	} );
	myTable.buttons().container().appendTo( $('.tableTools-container') );

	//style the message box
	var defaultCopyAction = myTable.button(1).action();
	myTable.button(1).action(function (e, dt, button, config) {
		defaultCopyAction(e, dt, button, config);
		$('.dt-button-info').addClass('gritter-item-wrapper gritter-info gritter-center white');
	});


	var defaultColvisAction = myTable.button(0).action();
	myTable.button(0).action(function (e, dt, button, config) {

		defaultColvisAction(e, dt, button, config);


		if($('.dt-button-collection > .dropdown-menu').length == 0) {
			$('.dt-button-collection')
			.wrapInner('<ul class="dropdown-menu dropdown-light dropdown-caret dropdown-caret" />')
			.find('a').attr('href', '#').wrap("<li />")
		}
		$('.dt-button-collection').appendTo('.tableTools-container .dt-buttons')
	});

	////

	setTimeout(function() {
		$($('.tableTools-container')).find('a.dt-button').each(function() {
			var div = $(this).find(' > div').first();
			if(div.length == 1) div.tooltip({container: 'body', title: div.parent().text()});
			else $(this).tooltip({container: 'body', title: $(this).text()});
		});
	}, 500);





	myTable.on( 'select', function ( e, dt, type, index ) {
		if ( type === 'row' ) {
			$( myTable.row( index ).node() ).find('input:checkbox').prop('checked', true);
		}
	} );
	myTable.on( 'deselect', function ( e, dt, type, index ) {
		if ( type === 'row' ) {
			$( myTable.row( index ).node() ).find('input:checkbox').prop('checked', false);
		}
	} );




	/////////////////////////////////
	//table checkboxes
	$('th input[type=checkbox], td input[type=checkbox]').prop('checked', false);

	//select/deselect all rows according to table header checkbox
	$('#dynamic-table > thead > tr > th input[type=checkbox], #dynamic-table_wrapper input[type=checkbox]').eq(0).on('click', function(){
		var th_checked = this.checked;//checkbox inside "TH" table header

		$('#dynamic-table').find('tbody > tr').each(function(){
			var row = this;
			if(th_checked) myTable.row(row).select();
			else  myTable.row(row).deselect();
		});
	});

	//select/deselect a row when the checkbox is checked/unchecked
	$('#dynamic-table').on('click', 'td input[type=checkbox]' , function(){
		var row = $(this).closest('tr').get(0);
		if(this.checked) myTable.row(row).deselect();
		else myTable.row(row).select();
	});



	$(document).on('click', '#dynamic-table .dropdown-toggle', function(e) {
		e.stopImmediatePropagation();
		e.stopPropagation();
		e.preventDefault();
	});



	//And for the first simple table, which doesn't have TableTools or dataTables
	//select/deselect all rows according to table header checkbox
	var active_class = 'active';
	$('#simple-table > thead > tr > th input[type=checkbox]').eq(0).on('click', function(){
		var th_checked = this.checked;//checkbox inside "TH" table header

		$(this).closest('table').find('tbody > tr').each(function(){
			var row = this;
			if(th_checked) $(row).addClass(active_class).find('input[type=checkbox]').eq(0).prop('checked', true);
			else $(row).removeClass(active_class).find('input[type=checkbox]').eq(0).prop('checked', false);
		});
	});

	//select/deselect a row when the checkbox is checked/unchecked
	$('#simple-table').on('click', 'td input[type=checkbox]' , function(){
		var $row = $(this).closest('tr');
		if($row.is('.detail-row ')) return;
		if(this.checked) $row.addClass(active_class);
		else $row.removeClass(active_class);
	});



	/********************************/
	//add tooltip for small view action buttons in dropdown menu
	$('[data-rel="tooltip"]').tooltip({placement: tooltip_placement});

	//tooltip placement on right or left
	function tooltip_placement(context, source) {
		var $source = $(source);
		var $parent = $source.closest('table')
		var off1 = $parent.offset();
		var w1 = $parent.width();

		var off2 = $source.offset();
		//var w2 = $source.width();

		if( parseInt(off2.left) < parseInt(off1.left) + parseInt(w1 / 2) ) return 'right';
		return 'left';
	}




	/***************/
	$('.show-details-btn').on('click', function(e) {
		e.preventDefault();
		$(this).closest('tr').next().toggleClass('open');
		$(this).find(ace.vars['.icon']).toggleClass('fa-angle-double-down').toggleClass('fa-angle-double-up');
	});
	/***************/





	/**
	//add horizontal scrollbars to a simple table
	$('#simple-table').css({'width':'2000px', 'max-width': 'none'}).wrap('<div style="width: 1000px;" />').parent().ace_scroll(
	  {
		horizontal: true,
		styleClass: 'scroll-top scroll-dark scroll-visible',//show the scrollbars on top(default is bottom)
		size: 2000,
		mouseWheelLock: true
	  }
	).css('padding-top', '12px');
	*/

	})
</script>
```


# 模板结构

1. base.html是通用模板文件
 - 引入需要的css,js文件
 - 包含header / leftnavi / footer 文件
 - 利用block content的方式，动态引入 主页面 部分
 - 利用block script的方式，动态引入 主页面部分需要的script

2. footer / header 是通用部分

3. leftnavi 是通用的左边导航栏，需要动态读取数据进行显示

4. query / queryscripts 是查询用的主页面，引入base框架，然后自定义content和script的block部分


# 显示效果如下：

![image](https://user-images.githubusercontent.com/18595935/30168859-9bbde19a-9425-11e7-8568-94b992d76493.png)
