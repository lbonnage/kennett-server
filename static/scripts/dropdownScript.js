$(function () {
    $("#serverDropdown").on("change", function () {
        switch ($(this).val()) {
            case "1":
                $("#divText").html("html/text for option 1");
                break;
            case "2":
                $("#divText").html("html/text for option 2");
                break;
            case "3":
                $("#divText").html("html/text for option 3");
                break;
            case "4":
                $("#divText").html("html/text for option 4");
                break;
        }
    });
});