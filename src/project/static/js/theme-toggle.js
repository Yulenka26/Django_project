const themeSwitch = document.getElementById('theme-switch');
const storedTheme = localStorage.getItem('theme');

if (storedTheme === 'dark') {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
    themeSwitch.checked = true;
} else {
    document.documentElement.setAttribute('data-bs-theme', 'light');
    themeSwitch.checked = false;
}

themeSwitch.addEventListener('change', () => {
    if (themeSwitch.checked) {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-bs-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
});
