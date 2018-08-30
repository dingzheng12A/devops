$(document).ready(function(){
    $("#dropUser").click(function(){
        $("#deluser").show()
            .siblings().hide();
        $("#userlist").DataTable();
    })
    $("#deluser table").on("click", "tr", function () {
        var $siblings = $(this).siblings('tr');
        $siblings.removeClass("selected").find('input[id="del_single"]').prop('disabled', true);
        $(this).addClass('selected').find('input[id="del_single"]').prop('disabled', false);
    })
     $("#deluser table").on("click", "tr #del_single", function () {
        var request = confirm("是否删除用户?");
        var $position = $(this).parent().parent();
        var userId = $(this).parent().siblings().find("#id").val();
        if (request == true) {
            $.ajax({
                type: 'post',
                url: '/deluser',
                data: {'userlist': userId},
                cache: false,
                dataType: 'json',
                success: function (data) {
                    $position.hide();
                    alert("用户已经删除!");

                }

            });
        }
        ;


    });
});