const sidebar_background = "black";
const sidebar_color = "white"

function page(element) {
    switch (element.id) {
        case "item-home": 
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            
            document.getElementById("item-user-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-user-background").style.background = sidebar_color;
            document.getElementById("item-user").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;            
            
            document.getElementById("item-admin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color;
            
            document.getElementById("item-settings").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color;
            
            document.getElementById("item-support").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color;
            
            document.getElementById("item-quit").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color;
            
            document.getElementById("item-comodin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-user": 
            document.getElementById("item-home-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-home-background").style.background = sidebar_color;
            document.getElementById("item-home").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;           
            
            document.getElementById("item-admin-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-admin-background").style.background = sidebar_color;
            document.getElementById("item-admin").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color;
            
            document.getElementById("item-settings").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color;
            
            document.getElementById("item-support").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color;
            
            document.getElementById("item-quit").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color;
            
            document.getElementById("item-comodin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-admin":
            document.getElementById("item-home").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            document.getElementById("item-user-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-user-background").style.background = sidebar_color;
            document.getElementById("item-user").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;           
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            
            document.getElementById("item-settings-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-settings-background").style.background = sidebar_color;
            document.getElementById("item-settings").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color;
            
            document.getElementById("item-support").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color;
            
            document.getElementById("item-quit").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color;
            
            document.getElementById("item-comodin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-settings":
            document.getElementById("item-home").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            document.getElementById("item-user").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;           
            
            document.getElementById("item-admin-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-admin-background").style.background = sidebar_color;
            document.getElementById("item-admin").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color; 
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            
            document.getElementById("item-support-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-support-background").style.background = sidebar_color;
            document.getElementById("item-support").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color;
            
            document.getElementById("item-quit").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color;
            
            document.getElementById("item-comodin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-support":
            document.getElementById("item-home").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            document.getElementById("item-user").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;              
            
            document.getElementById("item-admin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color;                       
            
            document.getElementById("item-settings-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-settings-background").style.background = sidebar_color;
            document.getElementById("item-settings").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color; 
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            
            document.getElementById("item-quit-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-quit-background").style.background = sidebar_color;
            document.getElementById("item-quit").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color;
            
            document.getElementById("item-comodin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-quit":
            document.getElementById("item-home").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            document.getElementById("item-user").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;              
            
            document.getElementById("item-admin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color;
            
            document.getElementById("item-settings").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color;
            
            document.getElementById("item-support-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-support-background").style.background = sidebar_color;
            document.getElementById("item-support").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color; 
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            
            document.getElementById("item-comodin-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-comodin-background").style.background = sidebar_color;
            document.getElementById("item-comodin").style.borderRadius = "30px 40px 0px 30px";
            document.getElementById("item-comodin").style.background = sidebar_background;
            document.getElementById("item-comodin").style.color = sidebar_color;
            break;
        case "item-comodin":
            document.getElementById("item-home").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-home").style.background = sidebar_background;
            document.getElementById("item-home").style.color = sidebar_color;
            
            document.getElementById("item-user").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-user").style.background = sidebar_background;
            document.getElementById("item-user").style.color = sidebar_color;             
            
            document.getElementById("item-admin").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-admin").style.background = sidebar_background;
            document.getElementById("item-admin").style.color = sidebar_color;
            
            document.getElementById("item-settings").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-settings").style.background = sidebar_background;
            document.getElementById("item-settings").style.color = sidebar_color;
            
            document.getElementById("item-support").style.borderRadius = "30px 0px 0px 30px";
            document.getElementById("item-support").style.background = sidebar_background;
            document.getElementById("item-support").style.color = sidebar_color;
            
            document.getElementById("item-quit-background").style.borderRadius = "35px 0px 0px 35px";
            document.getElementById("item-quit-background").style.background = sidebar_color;
            document.getElementById("item-quit").style.borderRadius = "30px 0px 40px 30px";
            document.getElementById("item-quit").style.background = sidebar_background;
            document.getElementById("item-quit").style.color = sidebar_color; 
            
            element.style.borderRadius = "30px 0px 0px 30px";
            element.style.background = sidebar_color;
            element.style.color = sidebar_background;
            break;
    }
}