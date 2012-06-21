var REG_EMAIL = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i;

$(function() {
    // login
    var login_email = $("#id_login_email");
    var login_pw = $("#id_login_pw");
    var login_checked = true;
    var password = login_pw.val();

    login_email.blur(function() {
        if(login_email.val() === ''){
            $(".email-error").html("请输入邮箱地址");
            login_checked = false;
        }else if(!REG_EMAIL.test(login_email.val())){
            $(".email-error").html("箱邮格式不正确");
            login_checked = false;
        }else{
            $(".email-error").html("");
        }
    })

    login_pw.blur(function(){
        //var password = login_pw.val();
        if(login_pw.val() === ''){
            $(".pw-error").html("请输入密码");
            login_checked = false;
        }else if(password.length < 6){
            $(".pw-errow").html("密码不能小于六个字符");
            login_checked = false;
        }else{
            $(".pw-error").html("");
        }
    })

    $(".login_form").submit(function(){
        login_checked=true;
        login_email.blur();
        login_pw.blur();

        return login_checked;
    });
});

