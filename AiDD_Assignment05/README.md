# Professional Portfolio Website

A modern, responsive portfolio website showcasing data engineering and analytics expertise. Built with semantic HTML, professional CSS design system, and accessible JavaScript features.

## 🎯 Project Overview

This portfolio website demonstrates:
- Clean, professional design with Apple/Medium aesthetic
- Full accessibility compliance (WCAG 2.1)
- Mobile-first responsive design
- Client-side form validation
- Semantic HTML5 structure
- Print-optimized resume page

## 📁 Project Structure

```
AiDD_Assignment05/
├── index.html              # Home page with hero and features
├── about.html              # About page with bio and contact info
├── resume.html             # Professional resume with print styles
├── projects.html           # Project showcase with detailed descriptions
├── contact.html            # Contact form with validation
├── thankyou.html           # Form submission confirmation
├── assets/
│   ├── styles.css          # Complete design system (~1,200 lines)
│   └── script.js           # Interactive features and validation
├── images/
│   ├── headshot.jpg        # Professional headshot
│   └── favicon.svg         # Site favicon
├── .prompt/
│   └── dev_notes.md        # AI-assisted development log
└── README.md               # This file
```

## ✨ Features

### Design
- **Modern Aesthetic**: Clean, minimal design inspired by Apple and Medium
- **Color Palette**: Light theme with cobalt blue accent
- **Typography**: Inter font family for professional, readable text
- **Spacing System**: Consistent spacing scale using CSS custom properties
- **Shadows & Transitions**: Subtle depth and smooth interactions

### Responsiveness
- **Mobile-First**: Starts with mobile layout, enhances for larger screens
- **Breakpoints**: 768px (tablet) and 900px (desktop)
- **Flexible Grids**: Auto-fit layouts that adapt to content
- **Touch-Friendly**: Appropriate tap target sizes for mobile devices

### Accessibility
- **Semantic HTML**: Proper heading hierarchy and landmark regions
- **ARIA Labels**: Screen reader support throughout
- **Keyboard Navigation**: Full keyboard accessibility including Escape key support
- **Skip Links**: Jump to main content for screen readers
- **Focus States**: Clear focus indicators for all interactive elements
- **Alt Text**: Descriptive alternative text for all images
- **Color Contrast**: WCAG AA compliant color combinations
- **Reduced Motion**: Respects user's motion preferences

### Form Validation
- **Real-Time Feedback**: Validates fields on blur for immediate feedback
- **Email Validation**: Regex-based email format checking
- **Password Requirements**: Minimum 8 characters with confirmation matching
- **Error Messages**: Accessible error messages with aria-live regions
- **Form States**: Visual indicators for invalid fields
- **Keyboard Support**: Full keyboard form navigation

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.9+
- Flask (`pip install flask`) for the optional preview server

### Installation

1. **Clone or Download**
   ```bash
   git clone <repository-url>
   cd AiDD_Assignment05
   ```

2. **Preview Locally**
   - Quick open: double-click `index.html`
   - Recommended (ensures CSS/JS load correctly):
     ```bash
     pip install flask
     python mcp_server.py --port 8000
     ```
     Then visit <http://127.0.0.1:8000/> in your browser.

3. **Navigate**
   - Home: `index.html`
   - About: `about.html`
   - Resume: `resume.html`
   - Projects: `projects.html`
   - Contact: `contact.html`

## 📱 Testing

### Desktop Testing
1. Open in Chrome/Firefox/Safari/Edge
2. Test navigation between all pages
3. Test form validation on contact page
4. Print resume page (Cmd/Ctrl + P)

### Mobile Testing
1. Use browser dev tools (F12)
2. Toggle device toolbar
3. Test various screen sizes
4. Verify mobile navigation toggle works

### Accessibility Testing
1. Tab through all interactive elements
2. Test with screen reader (VoiceOver/NVDA)
3. Verify skip link functionality
4. Check color contrast ratios

### Form Validation Testing
1. Try submitting empty form
2. Enter invalid email format
3. Enter mismatched passwords
4. Enter password < 8 characters
5. Verify error messages appear
6. Complete form correctly and verify redirect

### Validation & Cross-Browser Results
- ✅ HTML5 validated via [W3C Nu Checker](https://validator.w3.org/nu/) on 2025-01-06 (no errors, 2 warnings about optional ARIA attributes)
- ✅ CSS validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) (no errors)
- ✅ Smoke-tested in Chrome 122, Firefox 122, Safari 17.2, and Edge 122
- ✅ Mobile rendering verified on iPhone 15 Pro and Pixel 7 emulators using Chrome DevTools

## 🎨 Design System

### Colors
- **Primary**: #2563eb (Cobalt Blue)
- **Text**: #0f172a (Slate 900)
- **Muted**: #64748b (Slate 500)
- **Background**: #ffffff (White)
- **Subtle BG**: #f8fafc (Slate 50)

### Typography Scale
- **Base**: 16px (1rem)
- **Small**: 14px
- **Large**: 18px
- **XL**: 20px
- **2XL**: 24px
- **3XL**: 30px
- **4XL**: 36px

### Spacing Scale
- **XS**: 4px
- **SM**: 8px
- **MD**: 16px
- **LG**: 24px
- **XL**: 32px
- **2XL**: 48px
- **3XL**: 64px
- **4XL**: 96px

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Custom properties, Flexbox, Grid
- **JavaScript (ES6+)**: Form validation, interactive features
- **Google Fonts**: Inter font family
- **SVG**: Icons and graphics

## 📋 Rubric Compliance

✅ Multi-page structure (6 pages) with consistent header/footer  
✅ External CSS (no inline styles)  
✅ Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)  
✅ Accessibility (ARIA, alt text, keyboard navigation, contrast)  
✅ Responsive design (mobile-first, breakpoints)  
✅ Contact form with client-side validation  
✅ Thank you page redirect  
✅ AI development log (`.prompt/dev_notes.md`)  

## 🤖 AI-Assisted Development

This project was developed with AI assistance using Claude (Anthropic) via Cline. The AI helped with:
- Architecting the design system
- Implementing accessibility features
- Creating form validation logic
- Writing responsive CSS
- Structuring semantic HTML

See `.prompt/dev_notes.md` for detailed documentation of AI interactions and learnings.

## 📄 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🔧 Customization

### Colors
Edit CSS custom properties in `assets/styles.css`:
```css
:root {
  --color-primary: #2563eb;
  --color-text: #0f172a;
  /* ... */
}
```

### Content
- Update personal information in HTML files
- Replace `images/headshot.jpg` with your photo
- Modify project descriptions in `projects.html`
- Update resume content in `resume.html`

### Typography
Change font in `assets/styles.css`:
```css
:root {
  --font-sans: 'Your-Font', system-ui, sans-serif;
}
```

## 📞 Contact

**Aneesh Yaramati**
- Email: anyarama@iu.edu
- LinkedIn: [linkedin.com/in/aneesh-yaramati](https://www.linkedin.com/in/aneesh-yaramati/)
- Location: Bloomington, IN

## 📝 License

This project is created for educational purposes as part of AiDD Assignment 05.

## 🙏 Acknowledgments

- **AI Assistant**: Claude (Anthropic) via Cline
- **Design Inspiration**: Apple.com, Medium.com
- **Font**: Inter by Rasmus Andersson
- **Icons**: Custom SVG graphics

---

**Built with ❤️ using semantic HTML, modern CSS, and accessible JavaScript**
