$(document).ready(function () {
    $("#addRole").click(function () {
        $("#addrole").show()
            .siblings().hide();
        $("#rolearea").DataTable();
    })
    $("#addrole_btn").click(function () {
        $("#roleAddModal").modal({'show': true, backdrop: 'static', keyboard: false});
        $("#roleAddModal input[type='text']").val('');
        $("#roleAddModal input[type='textarea']").val('');
        $("#roleAddModal #cancle").click(function () {
            $("#roleAddModal").modal('hide');
        });
        $("#roleAddModal #rolename").bind("input propertychange change", function (event) {
            var rolename = $("#roleAddModal #rolename").val();


            if (rolename.length != 0) {
                $("#roleAddModal #add").attr("disabled", false);
            } else {

                $("#roleAddModal #add").attr("disabled", true);
            }
            ;
        });


        $("#roleAddModal #add").click(function () {
            var rolename = $("#roleAddModal #rolename").val();
            if (rolename.length == 0) {
                alert("角色和描述信息都不能为空!");
                $("#roleAddModal #add").attr("disabled", true);
            }


            $.ajax({
                type: 'post',
                url: '/addrole',
                data: {'rolename': rolename},
                cache: false,
                dataType: 'json',
                success: function (data) {
                    if (data['result'] == 1) {
                        alert("添加juese成功！");
                        //$("#roleAddModal").modal('hide');
                        window.location.href = "/roleinfo?page_role=1";

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
                    //window.location.href = msg.url;

                }
            });
        })
        ;


    });
    /* shanchu juese */
    $("#delRole").click(function () {
        $("#delrole").show()
            .siblings().hide();
        $("#rolelist").DataTable();
    })

    $("table[id='rolearea']").on("click", "tr", function () {
        var $siblings = $(this).siblings('tr');
        $siblings.removeClass("selected").find('button[id="delrole_commit"]').prop('disabled', true);
        $(this).addClass('selected').find('button[id="delrole_commit"]').prop('disabled', false);


    });

    $("table[id='rolelist']").on("click", "tr", function () {
        var $siblings = $(this).siblings('tr');
        $siblings.removeClass("selected").find('button[id="delrole_commit"]').prop('disabled', true);
        $(this).addClass('selected').find('button[id="delrole_commit"]').prop('disabled', false);


    });

    $("table[id='rolelist']").on("click", "tr #delrole_commit", function () {
        var container_users = $(this).parent().parent().children("td:eq(2)").text();
        var $position = $(this).parent().parent();
        var roleId = $(this).parent().siblings().find("#role_id").val();
        if (container_users.length > 0) {
            alert("角色中包含用户，不能删除!");
        }
        else {
            var request = confirm("是否删除角色?");


            if (request == true) {
                $.ajax({
                    type: 'post',
                    url: '/delrole',
                    data: {'rolelist': roleId},
                    cache: false,
                    dataType: 'json',
                    success: function (data) {
                        $position.hide();
                        alert("角色已经删除!");

                    }

                });
            }
            ;
        }
        ;


    });

//关联用户
    $("table[id='rolearea']").on("click", "tr #assign", function (e) {
        var rolename = $(this).parent().parent().children("td:eq(1)").text();
        var container_users = $(this).parent().parent().children("td:eq(2)").text();




        $("#userAssignRoleModal").modal({'show': true, backdrop: 'static', keyboard: false});
        var role_html = '';
        container_users.split(/\s+/).forEach(function(item, index) {
            item = item.trim();
            if (item) {
                role_html += '<span class="tag" data-value="'+item+'">'+item+'<a class="tag-remove">x</a></span>'
                }
        });


        $("#userAssignRoleModal #rolename").val(rolename);
        $("#userAssignRoleModal #container_user").val(container_users);
        $("#userAssignRoleModal #container_user").html(role_html);
        $("#userAssignRoleModal #add").click(function () {
            var select_user = $("#userAssignRoleModal").find("#userSelect").val();

            if (container_users.indexOf(select_user) < 0) {
                //container_users += select_user;
                //container_users += ' ';
                $("#userAssignRoleModal #container_user").append("<span class='tag' data-value='"+select_user+"'>"+select_user+"<a class=\"tag-remove\">x</a></span>");
            }

            //$("#userAssignRoleModal").find("#container_user").val(container_users);
            //$("#Layer_assign").hide(current_user);
        });


    })
    $("#userAssignRoleModal #cancle").click(function () {
        $("#userAssignRoleModal").modal('hide');
    });
    $("#userAssignRoleModal #confirm").off('click').on('click', function () {
        var rolename = $("#userAssignRoleModal #rolename").val();
        var userlist = [];
        $("#userAssignRoleModal #container_user span").each(function(){userlist.push($(this).text().replace(/x$/,''))});
        console.log(userlist);
        $.ajax({
            type: 'post',
            url: '/assign',
            data: {'userlist': userlist.join(" "), 'rolename': rolename},
            cache: false,
            dataType: 'json',
            success: function (data) {
                if (data.result == 1) {
                    alert("添加用户成功!");
                    $("#userAssignRoleModal ").modal('hide');
                    var selected = $("table tr[class='selected']");
                    var index = selected.index();
                    $("table[id='rolearea'] tr:eq(" + index + ")").children("td:eq(2)").text(userlist.join("    "));

                }
            }

        });
    })

//yichuguanlian
    $("table[id='rolearea']").on("click", "tr #remove", function (e) {
        var $selected = $("table[id='rolearea'] tr[class='selected']");
        var index = $selected.index();
        var rolename = $(this).parent().parent().children("td:eq(1)").text();
        var container_users = $(this).parent().parent().children("td:eq(2)").text();
        console.log("container_users:" + container_users);
        if (container_users.length > 0) {
            $("#removeAssignRoleModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
            $("#removeAssignRoleModal #rolename").val(rolename);

            var role_html = '';
            container_users.split(/\s+/).forEach(function(item, index) {
                item = item.trim();
                if (item) {
                    role_html += '<span class="tag" data-value="'+item+'">'+item+'<a class="tag-remove">x</a></span>'
                }
            });


            $("#removeAssignRoleModal #container_user").html(role_html);


            $("#removeAssignRoleModal #cancle").click(function () {
                $("#removeAssignRoleModal").modal('hide');
            });
            $("#removeAssignRoleModal #remove").click(function () {

                var container_users = $("#removeAssignRoleModal #container_user").val();
                var select_user = $("#removeAssignRoleModal #userSelect").val();
                // 从当前用户中删除选择的用户
                var newItemStr = removeSelectItem(select_user, container_users.replace(/^\s+/,'').replace(/\s+$/,'').split(/\s+/));
                console.log("split: "+container_users.replace(/^\s+/,'').replace(/\s+$/,'').split(/\s+/));

                $("#removeAssignRoleModal #container_user").val(newItemStr);
                // $("#removeAssignRoleModal #confirm").click(function () {
                //     var request = confirm("确定要移除用户吗?");
                //     if (request == true) {
                //         $.ajax({
                //             type: 'post',
                //             url: '/remove_assign',
                //             data: {'current_user': currentUser, 'roleid': roleid},
                //             cache: false,
                //             dataType: 'json',
                //             success: function (data) {
                //                 alert('success!');
                //                 $(".top").hide();
                //                 $("#Layer_remove").hide();
                //                 var selected = $("table tr[class='selected']");
                //                 var index = selected.index();
                //                 $("table[id='rolearea'] tr:eq(" + index + ")").children("td:eq(3)").text(currentUser);
                //             }
                //         })
                //
                //
                //     }
                // });

            })
            $('#removeAssignRoleModal').on('click', '.tag-remove', function () {
                $(this).parents('.tag').remove()
            })

            $("#removeAssignRoleModal #confirm").click(function(){
                var container_users=[];
                var index=$("table[id='rolearea'] tr[class='selected']").index();
                $('#removeAssignRoleModal #container_user .tag').each(function(idx, item){container_users.push($(item).data('value'))})
                $.ajax({
                    type: 'post',
                    url: '/removeassign',
                    data: {'rolename':rolename,'container_users': container_users.join(",")},
                    cache: false,
                    dataType: 'json',
                    success: function(data){
                        if(data.result==1){
                            console.log("Container_user: "+container_users);
                            $("#removeAssignRoleModal").modal('hide');
                            $("table[id='rolearea'] tr:eq(" + index + ")").children("td:eq(2)").text(container_users.join("    "));
                        }else{
                            alert("failure!");
                        }
                    }
                })

            })

        }

    })
});

function removeSelectItem(item, itemArr) {
    var i,len = itemArr.length, index;
    console.log("length iteArr:"+itemArr.length);
    for (i = 0; i < len; i++) {
        if (item == itemArr[i]) {
            index = i;
            break;
        }
    }
    if (index !== undefined) {
        itemArr.splice(index, 1);
    }

    return itemArr.join(' ');
};
