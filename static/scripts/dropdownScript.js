$(function () {
    $("#serverDropdown").on("change", function () {
        switch ($(this).val()) {
            case "1":
                $("#serverText").html("Server originally run by Rory.  Runs on Minecraft 1.7.10.  Requires the following:\n<a href=\"https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.7.10.html\">Forge Modloader 1.7.10</a>\n<a href=\"https://drive.google.com/open?id=1LsWumfkbwimx8a58t6UnC64iyqjzQKZj\">Mods</a>");
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