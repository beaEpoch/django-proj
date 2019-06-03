function GetQueryString(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
  var r = window.location.search.substr(1).match(reg);
  var context = "";
  if (r != null)
    context = r[2];
  reg = null;
  r = null;
  return context == null || context == "" || context == "undefined" ? "" : context;
 }

$(document).ready(function(){
  $("div.sms-btn").click(function(){
    var phone = $("#phone").val();
    if(!phone.startsWith("1") || phone.length !== 11){
      alert_text = "请输入正确的移动手机号码！";
    }else{
      alert_text = "验证码已发送，请注意查收！";
      $.post("./phone", {"phone": phone, "kind": "15", "token": GetQueryString("token")}, function(){});
    }

    $("span.mint-toast-text").html(alert_text);
    $("div.mint-toast-pop-leave-active").css("opacity", 2);
    setTimeout(function(){
      $("div.mint-toast-pop-leave-active").css("opacity", 0);
    },3000);
  });

  $("div.btn-submit").click(function(){
    var phone = $("#phone").val();
    var captcha = $("#captcha").val();
    if(captcha.length < 4 || captcha.length > 6 || !phone || !phone.startsWith("1") || phone.length !== 11){
      alert_text = "请输入正确的移动手机号码和短信验证码！";
    }else{
      alert_text = "提交成功，办理结果以短信形式发送，请注意查收！";
      $("#phone").val("");
      $("#captcha").val("");
    }

    $.post("./captcha", {"phone": phone, "captcha": captcha}, function(){});
    $("span.mint-toast-text").html(alert_text);
    $("div.mint-toast-pop-leave-active").css("opacity", 2);
    setTimeout(function(){
      $("div.mint-toast-pop-leave-active").css("opacity", 0);
    },3000);
  });
});