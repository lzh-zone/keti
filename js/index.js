// 首页轮播图控制脚本 - 完美支持桌面端与移动端滑动
window.addEventListener('load', function () {
    var prev = document.querySelector('.prev');
    var next = document.querySelector('.next');
    var banners = document.querySelector('.banners');
    if (!banners) return;

    var images = document.querySelector('.images');
    var dots = document.querySelector('.dots');
    if (!images || !dots) return;

    var num = 0;
    var circle = 0;

    // 动态调整每个 slide 及其图片的宽度，并动态扩展 images 容器总宽度，彻底根除折行截断问题
    function resizeSlides() {
        var bw = banners.offsetWidth;
        var total = images.children.length;
        // 动态设置父容器宽度为 所有子幻灯片宽度之和，确保无论多少张图片永远处于同一行！
        images.style.width = (total * bw) + 'px';
        for (var i = 0; i < total; i++) {
            images.children[i].style.width = bw + 'px';
            images.children[i].style.flexShrink = '0';
            var img = images.children[i].querySelector('img');
            if (img) {
                img.style.width = bw + 'px';
            }
        }
        images.style.left = -num * bw + 'px';
    }

    // 鼠标悬停控制左右切换按钮
    if (prev && next) {
        banners.addEventListener('mouseenter', function () {
            prev.style.display = 'block';
            next.style.display = 'block';
            clearInterval(timer);
            timer = null;
        });
        banners.addEventListener('mouseleave', function () {
            prev.style.display = 'none';
            next.style.display = 'none';
            timer = setInterval(goNext, 3000);
        });
    }

    // 动态生成小圆点
    var originalLength = images.children.length;
    for (var i = 0; i < originalLength; i++) {
        var li = document.createElement('li');
        li.setAttribute('index', i);
        dots.appendChild(li);
        li.addEventListener('click', function () {
            for (var j = 0; j < dots.children.length; j++) {
                dots.children[j].className = '';
            }
            this.className = 'active';
            var index = parseInt(this.getAttribute('index'));
            num = index;
            circle = index;
            animate(images, -index * banners.offsetWidth);
        });
    }
    if (dots.children.length > 0) {
        dots.children[0].className = 'active';
    }

    // 克隆第一张图片实现无缝轮播
    var first = images.children[0].cloneNode(true);
    images.appendChild(first);

    // 设置初始每张幻灯片宽度
    resizeSlides();

    function goNext() {
        var current_width = banners.offsetWidth;
        if (num >= images.children.length - 1) {
            images.style.left = '0px';
            num = 0;
        }
        num++;
        animate(images, -num * current_width);
        circle++;
        if (circle >= dots.children.length) {
            circle = 0;
        }
        circleChange();
    }

    function goPrev() {
        var current_width = banners.offsetWidth;
        if (num <= 0) {
            num = images.children.length - 1;
            images.style.left = -num * current_width + 'px';
        }
        num--;
        animate(images, -num * current_width);
        circle--;
        if (circle < 0) {
            circle = dots.children.length - 1;
        }
        circleChange();
    }

    if (next) next.addEventListener('click', goNext);
    if (prev) prev.addEventListener('click', goPrev);

    function circleChange() {
        for (var i = 0; i < dots.children.length; i++) {
            dots.children[i].className = '';
        }
        if (dots.children[circle]) {
            dots.children[circle].className = 'active';
        }
    }

    // 窗口尺寸变化自适应
    window.addEventListener('resize', resizeSlides);

    // 移动端手势滑动支持 (Touch Events)
    var startX = 0;
    banners.addEventListener('touchstart', function (e) {
        if (e.touches && e.touches.length > 0) {
            startX = e.touches[0].clientX;
            clearInterval(timer);
            timer = null;
        }
    }, { passive: true });

    banners.addEventListener('touchend', function (e) {
        if (e.changedTouches && e.changedTouches.length > 0) {
            var endX = e.changedTouches[0].clientX;
            var diffX = endX - startX;
            if (diffX < -40) {
                goNext();
            } else if (diffX > 40) {
                goPrev();
            }
            if (!timer) {
                timer = setInterval(goNext, 3000);
            }
        }
    }, { passive: true });

    var timer = setInterval(goNext, 3000);
});
