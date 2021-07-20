const sectionOne = document.querySelector('.progress');

const observer = new IntersectionObserver(
(entries) => {
    entries.forEach(entry => {
        if (entry.intersectionRatio > 0) {
            entry.target.classList.add('progress');
        } else {
            entry.target.classList.remove('progress');
        }
    });
});

 observer.observe(sectionOne);