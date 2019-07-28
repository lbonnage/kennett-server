$(function () {
    $("#serverDropdown").on("change", function () {
        switch ($(this).val()) {
            case "1":
                $("#serverText").html("html/text for option 1");
                break;
            case "2":
                $("#serverText").html("html/text for option 2");
                break;
            case "3":
                $("#serverText").html("html/text for option 3");
                break;
            case "4":
                $("#serverText").html("html/text for option 4");
                break;
        }
    });
});