# Design Systems

A structured path through design-system concepts, foundations, components, accessibility, implementation, governance, adoption, and decision-making.

## Topics

### 1. Foundations

- [ ] [ ] **DS-1.1** — Define a design system and explain the problems it is meant to solve.
- [ ] [ ] **DS-1.2** — Distinguish a design system from a style guide, pattern library, component library, and brand guide.
- [ ] [ ] **DS-1.3** — Describe the layers of a system: principles, foundations, tokens, components, patterns, and guidance.
- [ ] [ ] **DS-1.4** — Explain the benefits and costs of consistency across products and teams.
- [ ] [ ] **DS-1.5** — Distinguish visual consistency from coherence, usability, and accessibility.
- [ ] [ ] **DS-1.6** — Treat a design system as a product, including its users, value proposition, roadmap, and lifecycle.
- [ ] [ ] **DS-1.7** — Compare centralized, federated, and hybrid ownership models.
- [ ] [ ] **DS-1.8** — Define outcomes and signals that indicate whether a system is useful and healthy.

### 2. Foundations and Design Tokens

- [ ] [ ] **DS-2.1** — Explain design tokens and how they connect design decisions to implementation.
- [ ] [ ] **DS-2.2** — Distinguish primitive, semantic, and component-level tokens and when each layer helps.
- [ ] [ ] **DS-2.3** — Build color roles and palettes that support hierarchy, states, contrast, and themes.
- [ ] [ ] **DS-2.4** — Establish typography roles, type scales, line-height, and readable text measures.
- [ ] [ ] **DS-2.5** — Define spacing, sizing, grid, and layout scales that support predictable composition.
- [ ] [ ] **DS-2.6** — Specify shape, borders, elevation, and layering without relying on decoration alone.
- [ ] [ ] **DS-2.7** — Set principles for icons, imagery, and illustration, including sizing and meaning.
- [ ] [ ] **DS-2.8** — Define motion and transition principles, including reduced-motion preferences.
- [ ] [ ] **DS-2.9** — Design responsive breakpoints and density choices around content and behavior.
- [ ] [ ] **DS-2.10** — Support themes, brands, and modes without duplicating the entire system.

### 3. Components and Patterns

- [ ] [ ] **DS-3.1** — Distinguish a component from a pattern and choose the right level of abstraction.
- [ ] [ ] **DS-3.2** — Describe component anatomy, variants, properties, states, and interaction behavior.
- [ ] [ ] **DS-3.3** — Design component APIs that are composable, understandable, and appropriately constrained.
- [ ] [ ] **DS-3.4** — Define form controls, labels, validation, helper text, and error behavior as a coherent system.
- [ ] [ ] **DS-3.5** — Specify navigation, actions, selection, feedback, loading, empty, and error states.
- [ ] [ ] **DS-3.6** — Handle dialogs, menus, popovers, tooltips, and other layered interactions consistently.
- [ ] [ ] **DS-3.7** — Design data-display components such as tables, lists, badges, and status indicators.
- [ ] [ ] **DS-3.8** — Compose components into patterns for recurring user tasks and workflows.
- [ ] [ ] **DS-3.9** — Document purpose, anatomy, behavior, content guidance, examples, and appropriate use.
- [ ] [ ] **DS-3.10** — Recognize when a component is too narrow, too broad, or not reusable enough to belong in the system.

### 4. Accessibility and Inclusive Design

- [ ] [ ] **DS-4.1** — Apply inclusive-design principles when defining foundations, components, and patterns.
- [ ] [ ] **DS-4.2** — Use semantic structure and accessible names, roles, values, and relationships.
- [ ] [ ] **DS-4.3** — Design keyboard operation, focus order, visible focus, and focus management.
- [ ] [ ] **DS-4.4** — Meet contrast needs and avoid using color as the only way to convey meaning.
- [ ] [ ] **DS-4.5** — Make forms accessible with labels, instructions, required states, validation, and error summaries.
- [ ] [ ] **DS-4.6** — Communicate dynamic updates and status changes to assistive technologies.
- [ ] [ ] **DS-4.7** — Support zoom, reflow, text resizing, touch targets, and different input methods.
- [ ] [ ] **DS-4.8** — Respect motion preferences and avoid interaction patterns that cause barriers.
- [ ] [ ] **DS-4.9** — Combine automated checks, manual keyboard review, assistive-technology testing, and user feedback.
- [ ] [ ] **DS-4.10** — Use WCAG 2.2 as a testable reference while recognizing that conformance alone does not address every user need.

### 5. Design-to-Code and Quality

- [ ] [ ] **DS-5.1** — Organize design files, libraries, components, and variables for discoverability and reuse.
- [ ] [ ] **DS-5.2** — Establish a source of truth for tokens and transform them for different platforms.
- [ ] [ ] **DS-5.3** — Implement components with clear boundaries between structure, styling, behavior, and content.
- [ ] [ ] **DS-5.4** — Map design properties to code APIs and document intentional differences between platforms.
- [ ] [ ] **DS-5.5** — Publish documentation, examples, and interactive previews that support real implementation work.
- [ ] [ ] **DS-5.6** — Use unit, integration, and visual-regression testing for system components.
- [ ] [ ] **DS-5.7** — Test accessibility, keyboard behavior, responsive behavior, and important interaction states.
- [ ] [ ] **DS-5.8** — Package and distribute system assets so product teams can adopt compatible versions.
- [ ] [ ] **DS-5.9** — Apply versioning, release notes, and compatibility practices to design and code assets.
- [ ] [ ] **DS-5.10** — Detect and manage drift between design files, documentation, and production code.

### 6. Governance and Contribution

- [ ] [ ] **DS-6.1** — Define ownership, roles, decision rights, and responsibilities for system maintenance.
- [ ] [ ] **DS-6.2** — Create a contribution path that makes proposals, feedback, review, and status visible.
- [ ] [ ] **DS-6.3** — Evaluate proposals for user need, reuse across products, distinctiveness, and evidence.
- [ ] [ ] **DS-6.4** — Use research, design review, engineering review, and accessibility review in contribution decisions.
- [ ] [ ] **DS-6.5** — Balance consistency with legitimate product-specific needs and controlled extension points.
- [ ] [ ] **DS-6.6** — Manage deprecation, migration guidance, compatibility windows, and removal of outdated assets.
- [ ] [ ] **DS-6.7** — Maintain a clear roadmap, release history, support model, and known limitations.
- [ ] [ ] **DS-6.8** — Encourage contributions while preventing duplicate or unsupported components from fragmenting the system.
- [ ] [ ] **DS-6.9** — Prioritize system work using user impact, reach, risk, maintenance cost, and strategic fit.

### 7. Adoption and Evolution

- [ ] [ ] **DS-7.1** — Make system assets easy to discover, understand, and use in everyday product work.
- [ ] [ ] **DS-7.2** — Onboard teams with setup guidance, examples, support, and clear ownership expectations.
- [ ] [ ] **DS-7.3** — Plan incremental adoption and migration from existing product-specific UI.
- [ ] [ ] **DS-7.4** — Measure adoption and quality with usage data, contribution patterns, and product outcomes.
- [ ] [ ] **DS-7.5** — Gather feedback from product teams and end users, then turn it into system improvements.
- [ ] [ ] **DS-7.6** — Handle local extensions and overrides without losing upgrade paths or accessibility guarantees.
- [ ] [ ] **DS-7.7** — Support localization, content variation, and different regional or regulatory needs.
- [ ] [ ] **DS-7.8** — Scale a system across multiple products, platforms, teams, and brands.
- [ ] [ ] **DS-7.9** — Assess system maturity and choose an appropriate next step rather than maximizing process for its own sake.

### 8. Applying Design-System Principles

- [ ] [ ] **DS-8.1** — Decide whether a need calls for an existing component, a pattern, an extension, or a new contribution.
- [ ] [ ] **DS-8.2** — Assess a proposed component for user need, reuse, accessibility, maintainability, and fit.
- [ ] [ ] **DS-8.3** — Resolve a product requirement that conflicts with a system default or shared component API.
- [ ] [ ] **DS-8.4** — Diagnose duplicated UI and distinguish a system gap from a local product need.
- [ ] [ ] **DS-8.5** — Prioritize improvements when user impact, adoption, effort, and maintenance cost compete.
- [ ] [ ] **DS-8.6** — Plan a system rollout or migration with adoption measures and feedback loops.
- [ ] [ ] **DS-8.7** — Explain trade-offs between consistency, flexibility, accessibility, speed, and long-term maintenance.
- [ ] [ ] **DS-8.8** — Review a design-system decision and identify assumptions, evidence gaps, risks, and next steps.

## Reference Materials

Use these systems and standards as examples to compare. Their particular constraints do not automatically apply to every organization.

- [Web Content Accessibility Guidelines (WCAG) 2.2 — W3C](https://www.w3.org/TR/wcag/)
- [Design Tokens — U.S. Web Design System](https://designsystem.digital.gov/design-tokens/)
- [Components — GOV.UK Design System](https://design-system.service.gov.uk/components/)
- [Patterns — GOV.UK Design System](https://design-system.service.gov.uk/patterns/)
- [Contribution Criteria — GOV.UK Design System](https://design-system.service.gov.uk/community/contribution-criteria/)
