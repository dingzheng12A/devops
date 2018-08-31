$(document).ready(function () {
    $("#login").click(function () {
        var csrftoken = $.cookie('csrftoken');
        var $username = $("#username").val();
        var $password = $("#password").val();
        if ($username.length > 0 && $password.length > 0) {
            $.ajax({
                type: 'post',
                url: '/login/',
                data: {'username': $username, 'password': $password},
                //headers:{'X-CSRFToken':csrftoken},
                headers: {'X-CSRFToken': csrftoken},
                cache: false,
                dataType: 'json',
                success: function (data) {
                    if (data.result == 1) {
                        alert("密码验证成功.");
                        window.location.href = '/main';
                    } else {
                        alert("密码验证失败.");
                    }

                },
                failure: function (data) {
                    alert("密码验证失败!")
                }
            })

        }
    })
    $("#Logout").click(function () {
        $.ajax({
            type: 'get',
            url: '/logout',
            cache: false,
            dataType: 'json',
            success: function (data) {
                window.location.href = '/login';
            }
        })

    })

    $("#addUser").click(function () {
        $("#adduser").show()
            .siblings().hide();
        $("#userarea").DataTable();
    })

    $("#add_btn").click(function () {
        $("#userAddModal").modal({'show': true, backdrop: 'static', keyboard: false});

    })
    $("#userAddModal #cancle").click(function () {
        $("#userAddModal").modal('hide');
    })

    $("#userAddModal #username").bind("input propertychange change", function (event) {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal#nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();

        if (username.length != 0 && nicename.length != 0 && passwd.length != 0 && reptpass.length != 0 && email.length != 0 && (passwd == reptpass)) {
            $("#userAddModal #add").attr("disabled", false);
        } else {

            $("#userAddModal #add").attr("disabled", true);
        }
        ;
    });
    $("#userAddModal #nicename").bind("input propertychange change", function (event) {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal #nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();
        var email = $("#userAddModal #email").val();

        if (username.length != 0 && nicename.length != 0 && passwd.length != 0 && reptpass.length != 0 && email.length != 0 && (passwd == reptpass)) {
            $("#userAddModal #add").attr("disabled", false);
        } else {

            $("#userAddModal #add").attr("disabled", true);
        }
        ;
    });
    $("#userAddModal #passwd").bind("input propertychange change", function (event) {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal #nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();

        if (username.length != 0 && nicename.length != 0 && passwd.length != 0 && reptpass.length != 0 && email.length != 0 && (passwd == reptpass)) {
            $("#userAddModal #add").attr("disabled", false);
        } else {

            $("#userAddModal #add").attr("disabled", true);
        }
        ;
    });

    $("#userAddModal #reptpass").blur(function (event) {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal #nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();


        if (reptpass != passwd) {
            alert("两次输入的密码不一致!");
            $("#userAddModal #reptpass").focus();

            $("#userAddModal #add").attr("disabled", true);
        } else {
            $("#userAddModal #add").attr("disabled", false);
        }

    });

    $("#userAddModal #email").bind("input propertychange change", function (event) {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal #nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();

        if (username.length != 0 && nicename.length != 0 && passwd.length != 0 && reptpass.length != 0 && email.length != 0 && (passwd == reptpass)) {
            $("#userAddModal #add").attr("disabled", false);
        } else {

            $("#userAddModal #add").attr("disabled", true);
        }
        ;
    });

    $("#userAddModal #add").click(function () {
        var username = $("#userAddModal #username").val();
        var nicename = $("#userAddModal #nicename").val();
        var passwd = $("#userAddModal #passwd").val();
        var reptpass = $("#userAddModal #reptpass").val();
        var email = $("#userAddModal #email").val();
        var csrftoken = $.cookie('csrftoken');
        if (username.length == 0 || nicename.length == 0 || passwd.length == 0 || reptpass.length == 0 || email.length == 0) {
            alert("用户名和密码不能为空!");
            $("#userAddModal #add").attr("disabled", true);
        } else {
            if (passwd != reptpass) {
                alert("两次输入的密码不一致");
                $("#reptpass").focus();
                $("#userAddModal #add").attr("disabled", true);
            }
            else {
                $("#userAddModal #add").attr("disabled", false);
            }
        }
        ;


        $.ajax({
            type: 'post',
            url: '/adduser',
            data: {'username': username, 'nickname': nicename, 'passwd': passwd, 'email': email,},
            headers: {'X-CSRFToken': csrftoken},
            cache: false,
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 1) {
                    alert("添加用户成功！");
                    $("#userAddModal").modal('hide');
                    window.location.href = "/addUser/?page=1";


                } else {
                    alert("用户已经存在！");
                    $("#username").val('');
                    $("#nickname").val('');
                    $("#passwd").val('');
                    $("#reptpass").val('');
                    $("#email").val('');
                    $("#username").focus();
                    $("#Login").attr("disabled", true);
                }

            }
        });
    });
    $("table[id='userarea']").on("input propertychange change", "tr #resetpass", function (event) {
            var $position = $(this).parent().parent();
            var $newpass = $(this).val();

            if ($newpass.length > 0) {
                $position.find("#commit").attr("disabled", false);
            } else {
                $position.find("#commit").attr("disabled", true);
            }
        }
    )

    $("table[id='userarea']").on("click", "tr #commit", function () {
        var $position = $(this).parent().parent();
        var $newpass = $(this).parent().find("#resetpass").val();
        var $status = $(this).parent().find("#enable");
        var $username = $(this).parent().parent().children("td:eq(1)").text();
        console.log("username:" + $username);
        if ($status.is(":checked")) {
            var enable = 1;
            var status = "启用";
        } else {
            var enable = 0;
            var status = "禁用";
        }
        if ($newpass.length == 0) {
            $.ajax({
                type: 'post',
                url: '/setpass',
                data: {'username': $username, 'status': enable},
                cache: false,
                dataType: 'json',
                success: function (data) {
                    if (data.result == 1) {
                        alert("用户修改成功!");

                        $position.children("td:eq(3)").text(status);

                    }
                }

            });

        } else {
            var csrftoken = $.cookie('csrftoken');
            $.ajax({
                type: 'post',
                url: '/resetpass',
                data: {'username': $username, 'pwd': $newpass, 'status': enable},
                cache: false,
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',
                success: function (data) {
                    alert("用户修改成功!");
                    $position.children("td:eq(3)").text(status);
                }

            });


        }
    });

    $("table[id='userlist']").on("click", "tr", function () {
        var $siblings = $(this).siblings('tr');
        $siblings.removeClass("selected").find('button[id="del_single"]').prop('disabled', true);
        $(this).addClass('selected').find('button[id="del_single"]').prop('disabled', false);
        var csrftoken = $.cookie('csrftoken');
    })
    $("table[id='userlist']").on("click", "tr #del_single", function () {
        var csrftoken = $.cookie('csrftoken');
        var request = confirm("是否删除用户?");
        var $position = $(this).parent().parent();
        var userId = $(this).parent().siblings().find("#id").val();
        console.log("xxxxxxxxxxx");
        if (request == true) {
            $.ajax({
                type: 'post',
                url: '/deluser',
                data: {'userlist': userId},
                cache: false,
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',
                success: function (data) {
                    //$position.hide();
                    alert("用户已经删除!");
                    window.location.href = "/dropUser?page=1";

                }

            });
        }
        ;


    });

//piliangshanchuyonghu
    var num = 0;
    var userarray = [];
    $("table[id='userlist']").on("click", "tr #id", function () {

        if ($(this).is(":checked")) {
            num += 1;
            userarray[num] = $(this).val();
            console.log('点击次数:' + num + "userarray:" + userarray.join(" "));
        } else {
            userarray.pop($(this).val());
            num -= 1;
        }
        if (num > 0) {
            $("#deluser #del_btn").prop('disabled', false);
        } else {
            $("#deluser #del_btn").prop('disabled', true);
        }
    })
    $("#deluser #del_btn").click(function () {
        var csrftoken = $.cookie('csrftoken');
        console.log(userarray);
        console.log('点击次数:' + num);
        var request = confirm("是否删除用户?");
        if (request == true) {
            $.ajax({
                type: 'post',
                url: '/deluser',
                data: {'userlist': userarray.join(",").replace(/^,/, '')},
                cache: false,
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',
                success: function (data) {
                    window.location.href="/dropUser?page=1";


                }

            });
        }

    });


})
