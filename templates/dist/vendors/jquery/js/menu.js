$(document).ready(function () {
    $("#menu_add").click(function () {
        $("#menuAddModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});

    })

    $("div #menulist").on("click", "div button[id='add_submenu']", function () {
        $("#submenuAddModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
        var parent_id = $(this).siblings("input[type='hidden']").val();
        var parent_name = $(this).siblings("p").text();
        // console.log("parent_id:aaaaaaaaaa" + parent_id);
        $("form[id='submenu'] input[name='parentname']").val(parent_name);
        $("form[id='submenu'] input[name='parentid']").val(parent_id);

    })

    $("div #menulist").on("click", "div button[id='del_menu']", function () {
        var menuname = $(this).parent().children("p").text();
        var csrftoken = $.cookie('csrftoken');
        var childrenmenu = $(this).parent().siblings("ul").children(".row");
        if (childrenmenu.length==0) {
            $("#delmenuModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
            $("#delmenuModal button[type='submit']").click(function () {
                $.ajax({
                    type: 'post',
                    url: '/menumanager/delmenu/',
                    data: {'menuname': menuname},
                    cache: false,
                    headers: {'X-CSRFToken': csrftoken},
                    dataType: 'json',
                    success: function (data) {
                        if (data.result == 1) {
                            window.location.href = "/menumanager/addmenu/";
                        }

                    }
                });


            })
        } else {
            alert("aaaaaaaaaa");
            $("#menuwarning").alert();
        }


    })


    // shanchuzhicaidan
    $("div #menulist").on("click", "div button[id='del_submenu']", function () {
        var menuname = $(this).parent().children("p").text();
        var csrftoken = $.cookie('csrftoken');

        $("#delmenuModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
        $("#delmenuModal button[type='submit']").click(function () {
            $.ajax({
                type: 'post',
                url: '/menumanager/delmenu/',
                data: {'menuname': menuname},
                cache: false,
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',
                success: function (data) {
                    if (data.result == 1) {
                        window.location.href = "/menumanager/addmenu/";
                    }

                }

            });
        })
    })

    $("div #menulist").on("click", "div button[id='edit_submenu']", function () {
        var menuname = $(this).siblings("p").text();
        var url = $(this).siblings("input[name='menu_url']").val();
        var menu_id = $(this).siblings("input[name='menu_id']").val();
        $("#editmenuModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
        $("#editmenuModal #id_menuname").val(menuname);
        $("#editmenuModal #id_url").val(url);
        $("#editmenuModal #menu_id").val(menu_id);
        console.log("menuname:" + menuname + "url:" + url);
    })

})
