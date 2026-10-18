# Design System Specification

## 1. Overview & Creative North Star
This design system is anchored by a Creative North Star we define as **"The Intelligent Canvas."** 

Moving away from the rigid, grid-locked structures of traditional SaaS, this system adopts a high-end editorial approach. It treats the interface as a living document where AI-driven insights are curated rather than just displayed. By prioritizing extreme white space, asymmetric balance, and a monochrome foundation punctuated by "Intelligence Violet," we create an environment that feels authoritative, silent, and deeply modern. 

The goal is to eliminate visual noise. We do not use borders to contain ideas; we use proximity and tonal depth to suggest relationships.

---

## 2. Colors: The Monochrome Foundation
The palette is rooted in a sophisticated range of grays and blacks, using purple as a surgical strike—only appearing where "newness" or "intelligence" is present.

### Tonal Strategy
- **Primary & Neutrals:** We utilize `primary` (`#5c5c5c`) and `on-background` (`#191c1d`) to establish a high-contrast hierarchy. The background remains light (`surface` at `#f8f9fa`) to maintain an airy, editorial feel.
- **The Intelligence Accent:** `secondary` (`#4648d4`) and `tertiary` (`#6d4e8f`) are reserved strictly for high-value AI interactions, such as "New" badges, active AI processing states, or generative highlights.
- **The "No-Line" Rule:** **Prohibit 1px solid borders for sectioning.** To separate a sidebar from a main feed, or a header from a hero, use a background shift (e.g., placing a `surface-container-low` panel against a `surface` background). 
- **Signature Textures:** For primary CTAs or the main AI input area, utilize a subtle gradient transitioning from `primary` to `primary-container`. This adds a "lithic" quality that flat color lacks.

---

## 3. Typography: The Editorial Voice
We pair the technical precision of **Inter** with the characterful, geometric authority of **Manrope**.

- **Display & Headlines (Manrope):** Used for large "Ask me anything" prompts and section headers (`display-lg` to `headline-sm`). These should be bold and confident, utilizing the `on-background` token.
- **Body & Labels (Inter):** Used for functional reading and metadata. Inter provides the legibility required for dense AI outputs.
- **Hierarchy through Scale:** Use extreme scale shifts. A `display-lg` (3.5rem) headline should sit comfortably near a `body-sm` (0.75rem) label to create a professional, "published" look.

---

## 4. Elevation & Depth: Tonal Layering
Depth in this system is not about physical height, but about **Clarity of Focus.**

- **The Layering Principle:** Achieve hierarchy by "stacking" surface tiers. Place a `surface-container-lowest` card on a `surface-container-low` background. This creates a soft, natural lift that feels integrated into the UI.
- **Ambient Shadows:** Shadows should be used only for floating elements (like a command palette). Use the `on-surface` color at 4% opacity with a 32px blur—mimicking a soft, natural glow rather than a harsh drop shadow.
- **The "Ghost Border" Fallback:** If containment is required for accessibility, use a "Ghost Border": the `outline-variant` token at 15% opacity. Never use 100% opaque borders.
- **Glassmorphism:** For floating AI tooltips or mobile navigation, use semi-transparent `surface` colors with a `backdrop-blur` of 12px. This ensures the "Intelligent Canvas" is always visible beneath the active layer.

---

## 5. Components: Precision & Intent

### The AI Input Field (The Hero)
- **Styling:** Unlike standard text boxes, this should be a large, `surface-container-lowest` area with a `xl` (1.5rem) corner radius. 
- **Icons:** Use a mix of a solid "Spark" icon to denote AI power and an outlined "Send" icon for action.

### Buttons & Interaction
- **Primary:** Solid `on-primary-fixed` (`#1b1b1b`) with white text. Use `DEFAULT` (0.5rem) roundedness for a modern, architectural feel.
- **Secondary (The AI State):** Use the `secondary_container` (`#6063ee`) for buttons that trigger generative features.
- **Tertiary:** Text-only with an underline that appears only on hover, maintaining the minimalist aesthetic.

### Chips & Badges
- **The "New" Badge:** Small, `tertiary_fixed` (`#efdbff`) background with `on-tertiary-fixed` text. This is the only "color" permitted in a standard list view to draw the eye instantly to fresh content.

### Cards & Lists
- **Rule:** Forbid divider lines. 
- **Execution:** Separate list items using `spacing-4` (1.4rem). To group items (like "Featured" vs "Bookmarks"), use a subtle `surface-container-high` background for the entire group, allowing the negative space to define the boundaries.

---

## 6. Do's and Don'ts

### Do:
- **Use Intentional Asymmetry:** Let the left side of the screen breathe more than the right to guide the eye toward the "Ask" action.
- **Embrace White Space:** If you think there is enough space, add 20% more. Space is a luxury brand indicator.
- **Mix Icon Weights:** Pair a bold, solid icon (for the category) with a light, outlined icon (for the action) to create visual texture.

### Don't:
- **No Heavy Outlines:** Never wrap a card in a high-contrast black border. It breaks the "canvas" feel.
- **No Pure Black (#000):** Use `on-background` (`#191c1d`) for text to avoid visual vibration and eye strain.
- **Don't Over-Purple:** If everything is purple, nothing is "New." Use the accent color only for the specific delta of change or AI-specific interactions.