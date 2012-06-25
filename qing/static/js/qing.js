var REG_EMAIL = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i;

$(function() {
    // login
    var login_email = $("#id_login_email");
    var login_pw = $("#id_login_pw");
    var login_checked = true;

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
        if(login_pw.val() === ''){
            $(".pw-error").html("请输入密码");
            login_checked = false;
        }else if(login_pw.val().length < 6){
            $(".pw-error").html("密码不能小于六个字符");
            login_checked = false;
        }else{
            $(".pw-error").html("");
        }
    })

    $(".login-form").submit(function(){
        login_checked=true;
        login_email.blur();
        login_pw.blur();

        return login_checked;
    });

    // reg
    var reg_email = $("#id_reg_email");
    var reg_pw = $("#id_reg_pw");
    var reg_checked=true;

    reg_email.blur(function() {
        if(reg_email.val() === ''){
            $(".email-error").html("请输入邮箱地址");
            reg_checked = false;
        }else if(!REG_EMAIL.test(reg_email.val())){
            $(".email-error").html("箱邮格式不正确");
            reg_checked = false;
        }else{
            $.ajax({
                url: '/auth/ckemail',
                data: {'email': reg_email.val()},
                type: 'post',
                success: function(data){
                    if(data=='1'){
                        $(".email-error").html("该邮件已被注册");
                        reg_checked=false;
                        alert(reg_checked);
                    }else{
                        $(".email-error").html("");
                    }
                }
            });
        }
    })

    reg_pw.blur(function(){
        if(reg_pw.val() === ''){
            $(".pw-error").html("请输入密码");
            reg_checked = false;
        }else if(reg_pw.val().length < 6){
            $(".pw-error").html("密码不能小于六个字符");
            reg_checked = false;
        }else{
            $(".pw-error").html("");
        }
    })

    $(".reg-form").submit(function(){
        reg_checked=true;
        reg_email.blur();
        reg_pw.blur();
        return reg_checked;

    });
});

