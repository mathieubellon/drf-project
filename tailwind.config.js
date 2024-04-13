/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    /* Process all JavaScript files in django_app. */
    'core/**/*.{js,jsx,ts,tsx,vue}',
    'core/**/templates/**/*.html',
    'templates/**/*.html',
    'core/**/*.py',

    /* Ignore any JavaScript in node_modules folder. */
    '!**/node_modules',

    /* Process all JavaScript files in vite_app src. */
    'src/**/*.{js,jsx,ts,tsx,vue}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
};