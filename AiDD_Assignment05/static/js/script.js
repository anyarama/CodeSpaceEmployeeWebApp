/**
 * Professional Portfolio JavaScript
 * Built with AI assistance for AiDD Assignment 05
 * Handles navigation, form validation, and interactive elements
 */

// ============================================================================
// Mobile Navigation Toggle
// ============================================================================
(function initMobileNav() {
  const navToggle = document.getElementById('navToggle');
  const primaryNav = document.getElementById('primaryNav');
  
  if (!navToggle || !primaryNav) return;
  
  navToggle.addEventListener('click', () => {
    const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!isExpanded));
    primaryNav.classList.toggle('open', !isExpanded);
  });
  
  // Close mobile nav when clicking outside
  document.addEventListener('click', (event) => {
    if (!navToggle.contains(event.target) && !primaryNav.contains(event.target)) {
      navToggle.setAttribute('aria-expanded', 'false');
      primaryNav.classList.remove('open');
    }
  });
  
  // Close mobile nav on escape key
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && primaryNav.classList.contains('open')) {
      navToggle.setAttribute('aria-expanded', 'false');
      primaryNav.classList.remove('open');
      navToggle.focus();
    }
  });
})();

// ============================================================================
// Footer Copyright Year
// ============================================================================
(function updateCopyrightYear() {
  const yearElement = document.getElementById('year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }
})();

// ============================================================================
// Contact Form Validation
// ============================================================================
(function initContactForm() {
  const contactForm = document.getElementById('contactForm');
  
  if (!contactForm) return;
  
  // Form fields
  const firstName = document.getElementById('firstName');
  const lastName = document.getElementById('lastName');
  const email = document.getElementById('email');
  const password = document.getElementById('password');
  const confirmPassword = document.getElementById('confirmPassword');
  
  // Error message elements
  const firstNameError = document.getElementById('firstNameError');
  const lastNameError = document.getElementById('lastNameError');
  const emailError = document.getElementById('emailError');
  const passwordError = document.getElementById('passwordError');
  const confirmPasswordError = document.getElementById('confirmPasswordError');
  
  /**
   * Validates a single form field
   */
  function validateField(field, errorElement, validationFn, errorMessage) {
    const isValid = validationFn(field.value);
    
    if (!isValid) {
      field.setAttribute('aria-invalid', 'true');
      errorElement.textContent = errorMessage;
      return false;
    } else {
      field.removeAttribute('aria-invalid');
      errorElement.textContent = '';
      return true;
    }
  }
  
  /**
   * Validation functions
   */
  const validators = {
    required: (value) => value.trim().length > 0,
    email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
    minLength: (value, min) => value.length >= min,
    nameCharacters: (value) => /^[A-Za-z\s'-]+$/.test(value),
    passwordStrength: (value) => /^(?=.*[A-Za-z])(?=.*\d).{8,}$/.test(value),
    passwordsMatch: (password, confirm) => password === confirm && /^(?=.*[A-Za-z])(?=.*\d).{8,}$/.test(password)
  };
  
  /**
   * Real-time validation on blur
   */
  if (firstName && firstNameError) {
    firstName.addEventListener('blur', () => {
      if (!validators.required(firstName.value)) {
        validateField(
          firstName,
          firstNameError,
          validators.required,
          'First name is required'
        );
      } else {
        validateField(
          firstName,
          firstNameError,
          validators.nameCharacters,
          'Please use letters, spaces, apostrophes, or hyphens only'
        );
      }
    });
  }
  
  if (lastName && lastNameError) {
    lastName.addEventListener('blur', () => {
      if (!validators.required(lastName.value)) {
        validateField(
          lastName,
          lastNameError,
          validators.required,
          'Last name is required'
        );
      } else {
        validateField(
          lastName,
          lastNameError,
          validators.nameCharacters,
          'Please use letters, spaces, apostrophes, or hyphens only'
        );
      }
    });
  }
  
  if (email && emailError) {
    email.addEventListener('blur', () => {
      if (!validators.required(email.value)) {
        validateField(
          email,
          emailError,
          validators.required,
          'Email is required'
        );
      } else {
        validateField(
          email,
          emailError,
          validators.email,
          'Please enter a valid email address'
        );
      }
    });
  }
  
  if (password && passwordError) {
    password.addEventListener('blur', () => {
      validateField(
        password,
        passwordError,
        validators.passwordStrength,
        'Password must be 8+ characters with at least one letter and one number'
      );
    });
    
    // Clear confirm password error when password changes
    password.addEventListener('input', () => {
      if (confirmPassword.value && confirmPasswordError) {
        confirmPasswordError.textContent = '';
        confirmPassword.removeAttribute('aria-invalid');
      }
    });
  }
  
  if (confirmPassword && confirmPasswordError) {
    confirmPassword.addEventListener('blur', () => {
      if (!validators.required(confirmPassword.value)) {
        validateField(
          confirmPassword,
          confirmPasswordError,
          validators.required,
          'Please confirm your password'
        );
      } else if (!validators.passwordStrength(confirmPassword.value)) {
        validateField(
          confirmPassword,
          confirmPasswordError,
          () => false,
          'Password must be 8+ characters with at least one letter and one number'
        );
      } else if (password && confirmPassword.value !== password.value) {
        validateField(
          confirmPassword,
          confirmPasswordError,
          () => false,
          'Passwords do not match'
        );
      } else {
        confirmPassword.removeAttribute('aria-invalid');
        confirmPasswordError.textContent = '';
        // Also clear password error if it was set
        if (password && passwordError) {
          password.removeAttribute('aria-invalid');
          passwordError.textContent = '';
        }
      }
    });
  }
  
  /**
   * Form submission handler
   */
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    
    let isFormValid = true;
    
    // Validate first name
    if (firstName && firstNameError) {
      let firstNameValid = validateField(
        firstName,
        firstNameError,
        validators.required,
        'First name is required'
      );
      if (firstNameValid) {
        firstNameValid = validateField(
          firstName,
          firstNameError,
          validators.nameCharacters,
          'Please use letters, spaces, apostrophes, or hyphens only'
        );
      }
      if (!firstNameValid) {
        isFormValid = false;
        if (document.activeElement !== firstName) {
          firstName.focus();
        }
      }
    }
    
    // Validate last name
    if (lastName && lastNameError) {
      let lastNameValid = validateField(
        lastName,
        lastNameError,
        validators.required,
        'Last name is required'
      );
      if (lastNameValid) {
        lastNameValid = validateField(
          lastName,
          lastNameError,
          validators.nameCharacters,
          'Please use letters, spaces, apostrophes, or hyphens only'
        );
      }
      if (!lastNameValid) {
        isFormValid = false;
        if (!firstName || firstName.getAttribute('aria-invalid') !== 'true') {
          lastName.focus();
        }
      }
    }
    
    // Validate email
    if (email && emailError) {
      let isValid = true;
      if (!validators.required(email.value)) {
        isValid = validateField(
          email,
          emailError,
          validators.required,
          'Email is required'
        );
      } else {
        isValid = validateField(
          email,
          emailError,
          validators.email,
          'Please enter a valid email address'
        );
      }
      if (!isValid) {
        isFormValid = false;
        if (!firstName?.getAttribute('aria-invalid') && !lastName?.getAttribute('aria-invalid')) {
          email.focus();
        }
      }
    }
    
    // Validate password
    if (password && passwordError) {
      const isValid = validateField(
        password,
        passwordError,
        validators.passwordStrength,
        'Password must be 8+ characters with at least one letter and one number'
      );
      if (!isValid) {
        isFormValid = false;
        if (!firstName?.getAttribute('aria-invalid') && 
            !lastName?.getAttribute('aria-invalid') && 
            !email?.getAttribute('aria-invalid')) {
          password.focus();
        }
      }
    }
    
    // Validate confirm password
    if (confirmPassword && confirmPasswordError && password) {
      let errorMsg = '';
      let isValid = true;
      
      if (!validators.required(confirmPassword.value)) {
        errorMsg = 'Please confirm your password';
        isValid = false;
      } else if (!validators.passwordStrength(confirmPassword.value)) {
        errorMsg = 'Password must be 8+ characters with at least one letter and one number';
        isValid = false;
      } else if (confirmPassword.value !== password.value) {
        errorMsg = 'Passwords do not match';
        isValid = false;
      }
      
      if (!isValid) {
        confirmPassword.setAttribute('aria-invalid', 'true');
        confirmPasswordError.textContent = errorMsg;
        isFormValid = false;
        if (!firstName?.getAttribute('aria-invalid') && 
            !lastName?.getAttribute('aria-invalid') && 
            !email?.getAttribute('aria-invalid') &&
            !password?.getAttribute('aria-invalid')) {
          confirmPassword.focus();
        }
      } else {
        confirmPassword.removeAttribute('aria-invalid');
        confirmPasswordError.textContent = '';
      }
    }
    
    // If all validations pass, redirect to thank you page
    if (isFormValid) {
      // In a real application, you would submit the form data here
      // For this demo, we'll just redirect
      window.location.href = 'thankyou.html';
    }
  });
})();

// ============================================================================
// Smooth Scroll for Anchor Links
// ============================================================================
(function initSmoothScroll() {
  // Only apply to anchor links on the same page
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(event) {
      const href = this.getAttribute('href');
      
      // Skip if it's just "#"
      if (href === '#') return;
      
      const target = document.querySelector(href);
      
      if (target) {
        event.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
        
        // Update focus for accessibility
        target.focus({ preventScroll: true });
      }
    });
  });
})();

// ============================================================================
// Prefers Reduced Motion Check
// ============================================================================
(function checkReducedMotion() {
  const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  
  function handleMotionPreference() {
    if (mediaQuery.matches) {
      document.documentElement.style.setProperty('--transition-fast', '0ms');
      document.documentElement.style.setProperty('--transition-base', '0ms');
      document.documentElement.style.setProperty('--transition-slow', '0ms');
    }
  }
  
  // Check on load
  handleMotionPreference();
  
  // Listen for changes
  if (mediaQuery.addEventListener) {
    mediaQuery.addEventListener('change', handleMotionPreference);
  } else {
    // Fallback for older browsers
    mediaQuery.addListener(handleMotionPreference);
  }
})();

// ============================================================================
// Log to console (for debugging)
// ============================================================================
console.log('Portfolio JavaScript loaded successfully');
console.log('Built with AI assistance for AiDD Assignment 05');
