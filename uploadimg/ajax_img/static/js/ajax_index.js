
function imgPreview(fileDom,i){
    //console.log(document.getElementById('input_file').files[0]);
	if(window.FileReader){
		var reader = new FileReader()
	}else{
		//alert('此设备不支持图片浏览功能，如需该功能请升级您的设备！！！');
		layer.msg("此设备不支持图片浏览功能，如需该功能请升级您的设备！！！");
	}
	//获取文件
    var file = fileDom.files[0];
    console.log(file);
	//读取完成
	reader.onload = function(e){
		//图片路径设置为读取的图片
		//img.src=e.targer.result
		//console.log(document.getElementsByClassName('file-box'));
		document.getElementsByClassName('file-box')[i].style.background = "url("+e.target.result+")no-repeat";
		document.getElementsByClassName('file-box')[i].style.backgroundSize = '200px 200px';
		//console.log('reader',reader);
		layer.msg("图片 "+file.name+" 已选择");
	};
	reader.readAsDataURL(file);
}

$(document).ready(function(){
  $(".img_submit").on('click',function(){
    layer.msg("图片正在上传");
  });
});


