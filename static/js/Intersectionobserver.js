const sectionOne = document.querySelector('.start');

const observer = new IntersectionObserver(
(entries) => {
    entries.forEach(entry => {
        if (entry.intersectionRatio > 0) {
            entry.target.classList.add('start');
        } else {
            entry.target.classList.remove('start');
        }
    });
});

 observer.observe(sectionOne);

