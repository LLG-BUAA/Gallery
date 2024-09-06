document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab");
    const images = document.querySelectorAll(".image");
    const slider = document.querySelector(".image-slider");
    const toggleFooterBtn = document.getElementById("toggle-footer");
    const footerContainer = document.querySelector(".footer-container");

    let currentIndex = 0;

    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            document.querySelector(".tab.active").classList.remove("active");
            tab.classList.add("active");

            currentIndex = index;
            slider.style.transform = `translateX(-${index * 100}%)`; // 根据当前索引滑动图片
        });
    });

    toggleFooterBtn.addEventListener("click", () => {
        footerContainer.classList.toggle("collapsed");
    });
});
