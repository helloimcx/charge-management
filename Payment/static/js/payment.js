
  window.onload=function () {
		var input=$("#phone_input");
		input.focus();

    }

function changeimg(imgid) {
		       //初始化所有的图片



    $(".myimg").each(function(i,n){

            $(this).attr("src","/static/image/index_充值交费/"+"0"+(i+1)+".png");
            if($(this).attr("id")==imgid){
                $(this).attr("src","/static/image/index_充值交费/"+"1"+(i+1)+".png");//修改点击的那张图
            }
            switch(imgid){
				case 01:
				    $("#span1").text("10.00元");
				    $("#span2").text("10.00元");
				    $("#money").val(10);

				    break;
				case 02:
					$("#span1").text("30.00元");
				    $("#span2").text("30.00元");
				    $("#money").val(30);
				     break;
				case 03:
				     $("#span1").text("50.00元");
				     $("#span2").text("50.00元");
				     $("#money").val(50);
				      break;
				case 04:
				     $("#span1").text("100.00元");
				     $("#span2").text("100.00元");
				     $("#money").val(100);
				      break;
				case 05:
					 $("#span1").text("150.00元");
				     $("#span2").text("150.00元");
				     $("#money").val(150);
					break;
				case 06:
					 $("#span1").text("200.00元");
				     $("#span2").text("200.00元");
				     $("#money").val(200);
				      break;
				case 07:
					 $("#span1").text("300.00元");
				     $("#span2").text("300.00元");
				     $("#money").val(300);
				      break;
				case 08:
				     $("#span1").text("500.00元");
				     $("#span2").text("500.00元");
				     $("#money").val(500);
				      break;


			}
      });

        }

     $("#phone_input").focus(function () {
	      $("#message").html("");

      })




  function submit() {
	    if ($("#phone_input").val() == '') {
            layer.alert("请输入电话号码")
        }

		  if ($("#money").val() == 0) {
              layer.alert("请选择充值金额")
                }


          if($("#phone_input").val() != ''&&$("#money").val() != 0){
              var phone = $("#phone_input").val();

              $.post("/home/pay/", {'phone': phone}, function (ret) {

                  var result = ret.result;
                  if (result == 1) {
                      layer.open({
                          type: 2,
                          title: '确认充值订单',
                          maxmin: true,
                          shadeClose: true, //点击遮罩关闭层
                          area: ['800px', '350px'],
                          content: '/home/form',


                      });
                  }
                  else if (result == 0) {

                      $("#message").html("<span  class=\"alert alert-warning\"> <a href=\"#\" class=\"close\" data-dismiss=\"alert\">\n" +
                          "                                    &times;\n" +
                          "                                 </a>\n" +
                          "                                <strong>没有这个电话号码，请重新输入</strong></span>");
                  }
              })
          }


  }


