/*
 Toggle switch for light dark mode functionality
*/

const toggleSwitch = document.getElementById('checkbox');
const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
const themeText = document.getElementById('theme-text');

function switchTheme(e) {
    console.log('switchtheme');
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme','light');
        localStorage.setItem('theme','light');

    } else {
        document.documentElement.setAttribute('data-theme','dark');
        localStorage.setItem('theme','dark');
    }
}

if (currentTheme) {
    document.documentElement.setAttribute('data-theme',currentTheme);

    if ( currentTheme === 'light') {
        toggleSwitch.checked = true;

    } else {
        toggleSwitch.checked = false;
    }
}

toggleSwitch.addEventListener('change',switchTheme,false);
