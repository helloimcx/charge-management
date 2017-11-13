window.onload=function () {


layer.msg('充值成功!', {
            time: 2000
        }//不自动关闭
  ,function(){
    var index = parent.layer.getFrameIndex(window.name); //获取当前窗体索引
    parent.layer.close(index);

});

    }


