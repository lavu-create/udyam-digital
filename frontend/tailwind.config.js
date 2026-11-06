/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        airtel: {
          red: '#E40000',
          darkRed: '#B30000',
          lightRed: '#FFECEC',
          dark: '#111827',
          gray: '#4B5563',
          lightGray: '#F9FAFB',
          border: '#E5E7EB',
        }
      }
    },
  },
  plugins: [],
}

