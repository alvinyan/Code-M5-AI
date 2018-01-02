/*
* 调用摄像头
*/
function call_camera(){
    var video=document.getElementById("video");    
    var errocb=function(){  
        console.log("sth srong");  
    }  
    //调用电脑摄像头并将画面显示在网页  
    if(navigator.getUserMedia){  
        navigator.getUserMedia({"video":true},function(stream){  
            video.src=stream;  
            video.play();  
        },errocb);  
    }else if(navigator.webkitGetUserMedia){  
        navigator.webkitGetUserMedia({"video":true},function(stream){  
            video.src=window.webkitURL.createObjectURL(stream);  
            video.play();  
        },errocb);  
    }
}

