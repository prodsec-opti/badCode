(function() {
    var lastHeight = 0;

    window.sendCurrentWindowHeightToParent = function() {
        var newHeight = document.getElementById('content').offsetHeight;
        if (newHeight !== lastHeight) {
            lastHeight = newHeight;
            // window.parent.postMessage (height, "*");
            window.parent.postMessage(
                JSON.stringify(
                    {
                        source:'optiIFrame',
                        height: lastHeight
                    }
                ), "*");
        }
    };
