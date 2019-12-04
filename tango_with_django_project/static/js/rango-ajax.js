$('#likes').click(function(){
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/like_category/', {category_id: catid}, function(data){
		$('#like_count').html(data);
		$('#likes').hide();
	});
});

$('#suggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/suggest/',{ suggestion : query },function(data){
		$('#cats').html(data);
	});
});

$('.Rango-add').click(function(){
	var catid = $(this).attr("data-catid");
	var url = $(this).attr("data-url");
	var title = $(this).attr("data-title");
	var me = $(this)
	$.get('/add/',{catid:catid,url:url,title:title},function(data){
		$('#page').html(data);
		me.hide();
	});
});