$(function () {
    $("#serverDropdown").on("change", function () {
        switch ($(this).val()) {
        	case "0":
                $("#serverText").html("Select a server in the dropdown to see details here.");
                break;
            case "1":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.7.10.html\">Forge Modloader 1.7.10</a>";
            			var modslink = "<a href=\"https://drive.google.com/open?id=1LsWumfkbwimx8a58t6UnC64iyqjzQKZj\">Mods</a>";
            			return "Server originally run by Rory.  Runs on Minecraft 1.7.10.  Requires the following: " +
            			forgelink + ", " +
            			modslink;
            		}
            		)
                break;
            case "2":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/roguelike-adventures-and-dungeons\">Modpack</a>";
            			return "Roguelike Adventures and Dungeons modpack.  Runs on Minecraft 1.12.2.  If installing through Twitch launcher (easiest method) disregard following. Requires the following: " +
            			forgelink;
            		}
            		)
                break;
			case "3":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/sevtech-ages/files/2744522\">Modpack</a>"
						var twitchlink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/sevtech-ages/download/2744522?client=y\">Twitch launcher download</a>"
            			return "SevTech Ages 3.1.2 modpack.  Runs on Minecraft 1.12.2.<br> If installing through Twitch launcher (easiest method), make sure to click versions and choose '3.1.2' as the default is '3.0.8', and disregard the following.  Requires the following: " +
            			forgelink;
            		}
            		)
                break;
        }
    });
});