#!/usr/bin/env python3
"""
Generator script to produce exactly 300 test cases per suite for DiseaseGene:
  - tests/selenium/test_cases/test_cases.yml (SEL-001 -> SEL-300)
  - tests/appium/test_cases/test_cases.yml (APP-001 -> APP-300)
  - tests/load/test_cases/test_cases.yml (LOAD-001 -> LOAD-300)
  - tests/security/test_cases/test_cases.yml (SEC-001 -> SEC-300)
"""

import os
from pathlib import Path
import yaml

def generate_selenium_cases():
    cases = []
    
    # 1. Authentication & Session (SEL-001 - SEL-035) = 35
    auth_defs = [
        ("Valid Researcher Login", "authentication", "critical", "Verify valid login with researcher credentials", "User is authenticated and redirected to dashboard"),
        ("Valid Admin Login", "authentication", "critical", "Verify valid login with administrator credentials", "Admin dashboard is accessible with full admin rights"),
        ("Login with Invalid Password", "authentication", "high", "Verify login failure with incorrect password", "Error notification 'Incorrect username or password' displayed"),
        ("Login with Unregistered Username", "authentication", "high", "Verify login failure with non-existent username", "Authentication fails with 401 error message"),
        ("Login with Empty Username", "authentication", "medium", "Submit login form with blank username field", "Client-side validation highlights username as required"),
        ("Login with Empty Password", "authentication", "medium", "Submit login form with blank password field", "Client-side validation highlights password as required"),
        ("Login with Leading/Trailing Spaces in Username", "authentication", "low", "Enter username with surrounding whitespace", "Whitespace trimmed and login succeeds"),
        ("Password Masking Toggle", "authentication", "low", "Click password reveal eye icon on login form", "Password characters toggled between masked and cleartext"),
        ("Remember Me Checkbox State", "authentication", "low", "Check remember-me on login", "Session persistence cookie/token saved in local storage"),
        ("JWT Token Storage in Local Storage", "authentication", "high", "Inspect browser storage after successful login", "Bearer token is securely stored with valid expiry"),
        ("Logout Functionality", "authentication", "critical", "Click logout button in header user menu", "Session token cleared and user redirected to signin page"),
        ("Protected Route Redirect When Unauthenticated", "authentication", "high", "Directly navigate to /admin without login", "Redirected to /signin with redirect query param"),
        ("Valid User Registration", "authentication", "critical", "Submit valid registration form with new username and email", "Account created successfully and redirected to signin"),
        ("Register with Existing Username", "authentication", "high", "Submit registration with already taken username", "Error 'Username or email already registered' displayed"),
        ("Register with Existing Email", "authentication", "high", "Submit registration with already registered email", "Error 'Username or email already registered' displayed"),
        ("Register with Weak Password Under 8 Chars", "authentication", "medium", "Submit registration with password of 6 characters", "Validation rejects password shorter than 8 characters"),
        ("Register with Password Missing Uppercase", "authentication", "medium", "Submit registration without uppercase letters", "Validation requires at least one uppercase letter"),
        ("Register with Password Missing Numbers", "authentication", "medium", "Submit registration without numeric characters", "Validation requires at least one numeric digit"),
        ("Register with Password Missing Special Char", "authentication", "medium", "Submit registration without special characters", "Validation requires at least one special character"),
        ("Register with Mismatched Password Confirmation", "authentication", "medium", "Enter differing password and confirm password values", "Form shows 'Passwords do not match' error"),
        ("Register with Invalid Email Format", "authentication", "medium", "Enter email lacking @ or domain", "HTML5 and form validation flags invalid email"),
        ("Forgot Password Valid Email Submission", "authentication", "high", "Request password reset for valid registered email", "Success message 'If that email exists, a reset code has been sent' displayed"),
        ("Forgot Password Non-Existent Email", "authentication", "medium", "Request reset for non-existent email address", "Generic success message shown to prevent email enumeration"),
        ("Forgot Password Blank Email", "authentication", "low", "Submit forgot password with empty email input", "Field validation flags email as required"),
        ("Reset Password with Valid OTP", "authentication", "critical", "Submit email, 6-digit OTP, and new password", "Password reset successfully and login enabled with new password"),
        ("Reset Password with Invalid OTP", "authentication", "high", "Submit incorrect 6-digit OTP code", "Error 'Invalid or expired OTP' displayed"),
        ("Reset Password with Expired OTP", "authentication", "medium", "Submit reset form with expired verification code", "Error indicates OTP is invalid or expired"),
        ("Reset Password Weak New Password", "authentication", "medium", "Provide valid OTP but weak new password", "Password strength policy error prevents update"),
        ("Reset Password Confirmation Match", "authentication", "low", "Verify new password and confirmation match validation", "Submit disabled until fields match"),
        ("Session Expiration Notification", "authentication", "medium", "Simulate expired JWT token in browser storage", "User notified of session expiry and redirected to login"),
        ("Concurrent Login Handling", "authentication", "low", "Login from a secondary browser window", "Session token refreshed cleanly across tabs"),
        ("Clear Stuck User Endpoint Trigger", "authentication", "low", "Trigger clear-stuck-user cleanup utility", "Stuck user record removed if existing"),
        ("First Registered User Role Assignment", "authentication", "high", "Inspect role of initial database user", "First user assigned Admin role automatically"),
        ("Subsequent Registered User Role Assignment", "authentication", "high", "Inspect role of subsequent user", "Subsequent user assigned Researcher role"),
        ("User Profile Fetch on Signin", "authentication", "high", "Verify /api/v1/auth/me request upon signin", "User username, email, and role rendered in header"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(auth_defs, start=1):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 2. Navigation, Header & Layout (SEL-036 - SEL-065) = 30
    nav_defs = [
        ("Brand Logo Click Navigation", "navigation", "medium", "Click DiseaseGeneMap brand logo from any subpage", "Navigates directly to homepage /"),
        ("Header Navigation Link - Genes", "navigation", "high", "Click 'Genes' link in top navigation bar", "Navigates to /genes with active nav indicator"),
        ("Header Navigation Link - Diseases", "navigation", "high", "Click 'Diseases' link in top navigation bar", "Navigates to /diseases with active nav indicator"),
        ("Header Navigation Link - Associations", "navigation", "high", "Click 'Associations' link in top navigation bar", "Navigates to /associations page"),
        ("Header Navigation Link - Variants", "navigation", "high", "Click 'Variants' link in top navigation bar", "Navigates to /variants page"),
        ("Header Navigation Link - Pathways", "navigation", "high", "Click 'Pathways' link in top navigation bar", "Navigates to /pathways page"),
        ("Header Navigation Link - Drugs", "navigation", "medium", "Click 'Drugs' link in top navigation bar", "Navigates to /drugs page"),
        ("Header Navigation Link - Publications", "navigation", "medium", "Click 'Publications' link in top navigation bar", "Navigates to /publications page"),
        ("Header Navigation Link - Analytics", "navigation", "medium", "Click 'Analytics' link in top navigation bar", "Navigates to /analytics page"),
        ("Header Navigation Link - AI Insights", "navigation", "medium", "Click 'AI Insights' link in top navigation bar", "Navigates to /ai-insights network visualization"),
        ("Header Navigation Link - Database Explorer", "navigation", "medium", "Click 'Database' link in top navigation bar", "Navigates to /database page"),
        ("Header Navigation Link - Admin Overview", "navigation", "high", "Click 'Admin' link when logged in as Admin", "Navigates to /admin dashboard"),
        ("Admin Nav Hidden for Researcher", "navigation", "high", "Inspect header links when logged in as Researcher", "Admin link is hidden or restricted"),
        ("Dark/Light Theme Toggle", "ui", "medium", "Toggle theme switch in header", "HTML theme class toggles between dark and light modes"),
        ("Theme Persistence in LocalStorage", "ui", "low", "Refresh page after toggling dark theme", "Theme preference persists across page reloads"),
        ("Mobile Hamburger Menu Expand", "ui", "medium", "Resize viewport to mobile and click hamburger menu", "Mobile slide-over navigation drawer opens"),
        ("Mobile Hamburger Menu Collapse", "ui", "medium", "Click close button on mobile navigation drawer", "Mobile drawer closes smoothly"),
        ("Active Route Highlighting", "ui", "low", "Navigate to /genes and inspect nav tab styles", "Genes tab highlighted with active indicator styling"),
        ("Footer Links - About Us", "navigation", "low", "Click About link in footer", "Navigates to /about page"),
        ("Footer External Links Security", "ui", "low", "Inspect target and rel attributes of footer links", "External links contain rel='noopener noreferrer'"),
        ("Breadcrumb Navigation on Gene Detail", "navigation", "medium", "Navigate to /genes/BRCA1 and check breadcrumbs", "Breadcrumbs show Home > Genes > BRCA1 with valid links"),
        ("Breadcrumb Navigation on Disease Detail", "navigation", "medium", "Navigate to /diseases/DIS001 and check breadcrumbs", "Breadcrumbs show Home > Diseases > DIS001"),
        ("404 Error Page Rendering", "navigation", "medium", "Navigate to non-existent route /nonexistent-page", "Custom 404 page displayed with 'Back to Home' button"),
        ("404 Page Back Home Button Action", "navigation", "medium", "Click 'Return Home' button on 404 page", "Navigates successfully to / homepage"),
        ("Header Sticky Behavior on Scroll", "ui", "low", "Scroll down long page of items", "Header bar remains fixed/sticky at top of viewport"),
        ("Global Search Input in Header", "ui", "medium", "Inspect global search input in top navigation bar", "Search bar is present with placeholder 'Search genes, diseases...'"),
        ("Global Search Quick Enter Key Action", "navigation", "medium", "Type 'TP53' into header search and press Enter", "Navigates to /explorer?q=TP53 with search results"),
        ("User Avatar Dropdown Menu", "ui", "low", "Click user profile avatar in header", "Dropdown menu displays Profile, Settings, and Logout options"),
        ("Responsive Layout at 1280px (Desktop)", "ui", "low", "Set browser window width to 1280px", "Desktop grid layout displays without horizontal scrollbars"),
        ("Responsive Layout at 768px (Tablet)", "ui", "low", "Set browser window width to 768px", "Tablet responsive layout reorganizes cards into 2-column grid"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(nav_defs, start=36):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 3. Genes Module (SEL-066 - SEL-105) = 40
    gene_defs = [
        ("Genes Catalog Page Initial Load", "genes", "critical", "Navigate to /genes catalog page", "Genes table/grid loads with initial batch of genes"),
        ("Genes Table Column Headers", "genes", "high", "Verify table headers on genes page", "Columns: Symbol, Name, Chromosome, Function, Protein, Actions"),
        ("Genes Pagination Next Page", "genes", "high", "Click 'Next' button on genes list pagination", "Second page of genes loaded with updated skip offset"),
        ("Genes Pagination Previous Page", "genes", "medium", "Click 'Previous' button on page 2", "Returns to page 1 of genes catalog"),
        ("Genes Pagination Limit Selector", "genes", "medium", "Change items per page dropdown from 20 to 50", "Page refreshes displaying 50 gene records"),
        ("Genes Filter by Chromosome 1", "genes", "high", "Select 'Chr 1' in chromosome filter dropdown", "Table filters to show only genes on chromosome 1"),
        ("Genes Filter by Chromosome 7", "genes", "medium", "Select 'Chr 7' in chromosome filter", "Table displays CFTR and other Chr 7 genes"),
        ("Genes Filter by Chromosome 17", "genes", "medium", "Select 'Chr 17' in chromosome filter", "Table displays BRCA1 and other Chr 17 genes"),
        ("Genes Filter by Chromosome X", "genes", "medium", "Select 'Chr X' in chromosome filter", "Table displays X-linked gene entries"),
        ("Genes Filter by Chromosome Y", "genes", "medium", "Select 'Chr Y' in chromosome filter", "Table displays Y-linked gene entries"),
        ("Genes Clear Chromosome Filter", "genes", "medium", "Click 'Reset Filters' button on genes page", "All chromosome filters cleared, showing all genes"),
        ("Gene Search by Symbol 'BRCA1'", "genes", "critical", "Type 'BRCA1' in genes table search input", "Table filters to show BRCA1 record"),
        ("Gene Search by Full Name 'Tumor Protein'", "genes", "high", "Type 'Tumor Protein' in search box", "Table filters to show TP53 and related genes"),
        ("Gene Search Non-Existent Query", "genes", "medium", "Search for 'XYZNONEXISTENT999'", "Table displays 'No genes found matching your search'"),
        ("Click Gene Row to Open Detail View", "genes", "critical", "Click on gene row 'BRCA1'", "Navigates to /genes/BRCA1 or opens detail panel"),
        ("Gene Detail View Header and Symbol", "genes", "high", "Verify gene detail page title", "Displays gene symbol 'BRCA1' and full official name"),
        ("Gene Detail View Genomic Coordinates", "genes", "medium", "Inspect genomic coordinate section", "Displays chromosome, start position, end position, and strand"),
        ("Gene Detail View Biological Function", "genes", "medium", "Inspect gene function description card", "Displays molecular function and cellular role"),
        ("Gene Detail View Protein Product", "genes", "medium", "Inspect protein card on gene detail page", "Displays protein name, length, and UniProt ID link"),
        ("Gene Detail Associated Diseases List", "genes", "high", "Check associated diseases section on gene detail", "Lists linked diseases (e.g., Breast Cancer, Ovarian Cancer)"),
        ("Gene Detail Associated Variants List", "genes", "high", "Check variants tab on gene detail page", "Displays table of genetic variants associated with this gene"),
        ("Gene Detail Associated Pathways List", "genes", "medium", "Check pathways tab on gene detail page", "Displays metabolic and biological pathways (e.g., DNA Repair)"),
        ("Favorite Gene Click While Logged In", "genes", "high", "Click heart icon next to gene symbol as logged-in user", "Heart icon fills red; message 'Gene favorited successfully'"),
        ("Unfavorite Gene Action", "genes", "high", "Click favorited heart icon again to remove favorite", "Heart icon un-fills; message 'Gene unfavorited successfully'"),
        ("Favorite Gene Prompt for Anonymous User", "genes", "high", "Click heart icon while not authenticated", "Redirected to login or shown 'Authentication required' prompt"),
        ("Favorite Gene State Persists on Reload", "genes", "medium", "Reload gene detail page after favoriting", "Heart icon remains active/filled"),
        ("Gene Detail External Link to NCBI Gene", "genes", "low", "Click NCBI external reference button", "Opens NCBI Gene database in new browser tab"),
        ("Gene Detail External Link to Ensembl", "genes", "low", "Click Ensembl external reference button", "Opens Ensembl genome browser in new tab"),
        ("Gene Detail Copy Sequence/Symbol Button", "genes", "low", "Click copy button next to gene symbol", "Copies symbol to clipboard and shows toast 'Copied!'"),
        ("Gene Table Sort by Symbol Ascending", "genes", "medium", "Click 'Symbol' column header sort arrow", "Table re-sorts genes alphabetically A-Z"),
        ("Gene Table Sort by Symbol Descending", "genes", "medium", "Click 'Symbol' sort arrow again", "Table re-sorts genes Z-A"),
        ("Gene Table Sort by Chromosome", "genes", "medium", "Click 'Chromosome' column header", "Table sorts by numerical chromosome order"),
        ("Gene List Loading Skeleton Indicator", "genes", "medium", "Inspect table during page transition", "Skeleton placeholder rows displayed before data renders"),
        ("Gene Detail Back Button Action", "genes", "medium", "Click 'Back to Genes' button on detail page", "Returns to /genes retaining previous filter/pagination state"),
        ("Gene Favorite Count Badge in Header", "genes", "medium", "Favorite a gene and inspect header favorites badge", "Favorites count badge increments by 1"),
        ("Gene Detail Print / Export View", "genes", "low", "Click export/print button on gene detail page", "Generates printable view or downloads gene summary"),
        ("Gene Symbol Quick Filter Auto-Focus", "genes", "low", "Press '/' shortcut key on genes page", "Focus shifts immediately into search filter input"),
        ("Gene Detail 404 for Invalid Gene ID", "genes", "medium", "Navigate directly to /genes/INVALID_GENE_9999", "Shows 'Gene not found' error banner with back button"),
        ("Genes Catalog Empty State Reset Link", "genes", "low", "Filter by impossible criteria and click 'Clear filters'", "Filters reset and default catalog list reloaded"),
        ("Genes Catalog Responsive Mobile View", "genes", "medium", "View genes catalog on 375px mobile viewport", "Table converts to responsive card stack layout"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(gene_defs, start=66):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 4. Diseases Module (SEL-106 - SEL-140) = 35
    dis_defs = [
        ("Diseases Catalog Initial Load", "diseases", "critical", "Navigate to /diseases catalog page", "Diseases list loads with initial dataset"),
        ("Diseases Table Column Headers", "diseases", "high", "Verify table columns on diseases page", "Columns: Disease Name, Category, ICD Code, OMIM, Actions"),
        ("Diseases Pagination Next Page", "diseases", "high", "Click 'Next' button on diseases pagination", "Loads next page with incremented offset"),
        ("Diseases Pagination Previous Page", "diseases", "medium", "Click 'Previous' button on page 2", "Returns to previous page of diseases"),
        ("Disease Search by Name 'Alzheimer'", "diseases", "critical", "Type 'Alzheimer' in disease search input", "Filters to Alzheimer's Disease record"),
        ("Disease Search by Name 'Diabetes'", "diseases", "high", "Type 'Diabetes' in disease search", "Displays Type 1 and Type 2 Diabetes records"),
        ("Disease Search by ICD-10 Code 'E11'", "diseases", "high", "Search by ICD code 'E11'", "Displays matching diabetes disease records"),
        ("Disease Filter by Category 'Oncology'", "diseases", "high", "Select 'Cancer / Oncology' in category filter", "Table displays only cancer and neoplasm diseases"),
        ("Disease Filter by Category 'Cardiovascular'", "diseases", "high", "Select 'Cardiovascular' in category filter", "Table displays coronary artery and heart diseases"),
        ("Disease Filter by Category 'Neurological'", "diseases", "high", "Select 'Neurological' in category filter", "Table displays Alzheimer's, Parkinson's, ALS"),
        ("Disease Filter by Category 'Metabolic'", "diseases", "medium", "Select 'Metabolic' in category filter", "Table displays diabetes and metabolic syndromes"),
        ("Disease Filter Reset Action", "diseases", "medium", "Click 'Reset Filters' on diseases page", "All category filters cleared, showing all diseases"),
        ("Click Disease Row to Open Detail View", "diseases", "critical", "Click on disease record 'Breast Cancer'", "Navigates to /diseases/DIS001 or detail panel"),
        ("Disease Detail Header and Category Badge", "diseases", "high", "Inspect disease detail page header", "Displays disease title, category badge, and ICD code"),
        ("Disease Detail Clinical Description", "diseases", "medium", "Inspect clinical overview section", "Displays disease etiology and phenotypic description"),
        ("Disease Detail OMIM Link", "diseases", "medium", "Click OMIM identifier link", "Opens OMIM database entry in new browser window"),
        ("Disease Detail Associated Genes Table", "diseases", "high", "Inspect associated genes section on disease detail", "Lists linked genes (e.g. BRCA1, BRCA2, TP53)"),
        ("Disease Detail Click Associated Gene Link", "diseases", "high", "Click gene symbol link inside disease detail", "Navigates directly to that gene's detail page"),
        ("Disease Detail Associated Drugs Section", "diseases", "medium", "Inspect therapeutic drugs section on disease page", "Displays targeted therapies and clinical drug agents"),
        ("Favorite Disease Click While Logged In", "diseases", "high", "Click favorite star/heart on disease detail page", "Disease marked as favorite; toast notification shown"),
        ("Unfavorite Disease Action", "diseases", "high", "Click favorite button again to remove favorite", "Favorite status removed; toast notification shown"),
        ("Favorite Disease Anonymous User Handling", "diseases", "medium", "Click favorite button without signing in", "Prompts user to sign in to save favorites"),
        ("Favorite Disease State Saved Across Sessions", "diseases", "medium", "Reload disease detail after favoriting", "Favorite indicator remains active"),
        ("Disease Table Sort by Name Ascending", "diseases", "medium", "Click 'Disease Name' column header", "Diseases sorted alphabetically A-Z"),
        ("Disease Table Sort by Category", "diseases", "medium", "Click 'Category' column header", "Diseases grouped/sorted by clinical category"),
        ("Disease Detail 404 for Invalid Disease ID", "diseases", "medium", "Navigate to /diseases/INVALID_DIS_9999", "Displays 'Disease not found' error banner"),
        ("Disease Detail Back to Catalog Button", "diseases", "medium", "Click 'Back to Diseases' link", "Navigates back to /diseases maintaining filter state"),
        ("Disease Catalog Search Non-Existent Name", "diseases", "medium", "Search for 'NonExistentCondition404'", "Displays 'No diseases found matching query'"),
        ("Disease Detail Publication Citations", "diseases", "medium", "Inspect literature references section on disease page", "Displays linked PubMed publications"),
        ("Disease Detail Phenotype Tags", "diseases", "low", "Inspect clinical phenotype tag badges", "Badges render with appropriate styling"),
        ("Disease Detail Risk Factor Summary", "diseases", "low", "Inspect genetic risk factors card", "Summarizes known penetrance and risk ratios"),
        ("Disease Catalog Items Per Page Selector", "diseases", "low", "Select 100 items per page", "Table renders 100 disease rows"),
        ("Disease Catalog Quick Filter Clear Icon", "diseases", "low", "Click 'x' inside search input", "Search input cleared and list resets immediately"),
        ("Disease Detail External Link to Orphanet", "diseases", "low", "Click Orphanet link for rare diseases", "Opens Orphanet portal in external tab"),
        ("Disease Catalog Mobile Card View", "diseases", "medium", "View diseases page on mobile viewport", "Cards render with title, category badge, and tap target"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(dis_defs, start=106):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 5. Associations & Variants (SEL-141 - SEL-175) = 35
    assoc_var_defs = [
        ("Associations Table Initial Load", "associations", "critical", "Navigate to /associations explorer page", "Associations table loads with gene-disease pairs"),
        ("Associations Columns Verification", "associations", "high", "Verify table column structure", "Columns: Gene, Disease, Confidence Score, Evidence Level, Source"),
        ("Associations Filter by Evidence Level A", "associations", "high", "Select 'Level A - High Confirmed' filter", "Table displays only Level A verified associations"),
        ("Associations Filter by Evidence Level B", "associations", "medium", "Select 'Level B - Moderate' filter", "Table displays only Level B association records"),
        ("Associations Filter by Evidence Level C", "associations", "medium", "Select 'Level C - Preliminary' filter", "Table displays Level C associations"),
        ("Associations Filter by Evidence Level D", "associations", "low", "Select 'Level D - Computational' filter", "Table displays computationally predicted associations"),
        ("Associations Confidence Score Slider Filter", "associations", "high", "Adjust minimum confidence score slider to 0.8", "Table filters to associations with score >= 0.8"),
        ("Associations Sort by Confidence Score Descending", "associations", "high", "Click 'Confidence Score' column header", "Associations sorted from highest score (1.0) downwards"),
        ("Associations Sort by Confidence Score Ascending", "associations", "medium", "Click score sort arrow to reverse sort", "Associations sorted from lowest score upwards"),
        ("Associations Gene Filter Input", "associations", "high", "Filter associations by gene 'BRCA1'", "Displays only pairs involving BRCA1"),
        ("Associations Disease Filter Input", "associations", "high", "Filter associations by disease 'Ovarian Cancer'", "Displays only pairs involving Ovarian Cancer"),
        ("Associations Combined Filter (Gene + Score)", "associations", "high", "Filter by Gene 'TP53' and min score '0.75'", "Displays only TP53 associations meeting score threshold"),
        ("Associations Reset Filter Button", "associations", "medium", "Click 'Reset Filters' on associations page", "All slider and dropdown filters reset to defaults"),
        ("Associations Row Click Navigation to Gene", "associations", "medium", "Click gene chip inside association row", "Navigates to the corresponding gene detail page"),
        ("Associations Row Click Navigation to Disease", "associations", "medium", "Click disease chip inside association row", "Navigates to the corresponding disease detail page"),
        ("Associations Pagination Next Page", "associations", "medium", "Click Next on associations pagination", "Loads next page of association records"),
        ("Associations Empty Results Handling", "associations", "low", "Set confidence score to 1.0 with incompatible gene", "Shows 'No associations match current criteria'"),
        ("Variants Catalog Initial Load", "variants", "critical", "Navigate to /variants catalog page", "Variants catalog table loads with variant list"),
        ("Variants Column Headers Check", "variants", "high", "Inspect table column headers", "Columns: rsID, Gene, Mutation Type, Clinical Significance, Consequence"),
        ("Variants Filter by Mutation Type 'Missense'", "variants", "high", "Select 'Missense' in mutation type dropdown", "Table shows only missense variant records"),
        ("Variants Filter by Mutation Type 'Nonsense'", "variants", "medium", "Select 'Nonsense' in mutation dropdown", "Table shows stop-gain / nonsense variants"),
        ("Variants Filter by Mutation Type 'Frameshift'", "variants", "medium", "Select 'Frameshift' in mutation dropdown", "Table shows insertion/deletion frameshift variants"),
        ("Variants Filter by Mutation Type 'Synonymous'", "variants", "low", "Select 'Synonymous' in mutation dropdown", "Table shows synonymous coding variants"),
        ("Variants Filter by ClinSig 'Pathogenic'", "variants", "critical", "Filter by clinical significance 'Pathogenic'", "Table displays confirmed pathogenic variants in red badge"),
        ("Variants Filter by ClinSig 'Likely Pathogenic'", "variants", "high", "Filter by 'Likely Pathogenic'", "Table displays likely pathogenic variants in orange badge"),
        ("Variants Filter by ClinSig 'VUS'", "variants", "medium", "Filter by 'Variant of Uncertain Significance'", "Table displays VUS variants in yellow badge"),
        ("Variants Filter by ClinSig 'Benign'", "variants", "medium", "Filter by 'Benign'", "Table displays benign variants in green badge"),
        ("Variants Search by dbSNP rsID 'rs28897700'", "variants", "critical", "Enter rsID in variant search input", "Filters to specific variant record"),
        ("Variants Click Row to Open Detail Modal", "variants", "high", "Click on variant row in table", "Opens variant detail modal with HGVS nomenclature"),
        ("Variant Detail HGVS Coding Annotation", "variants", "medium", "Inspect HGVS coding annotation (e.g. c.181T>G)", "Annotation correctly formatted and displayed"),
        ("Variant Detail HGVS Protein Annotation", "variants", "medium", "Inspect HGVS protein annotation (e.g. p.Cys61Gly)", "Protein change annotation correctly displayed"),
        ("Variant Detail dbSNP External Reference", "variants", "low", "Click dbSNP link in variant modal", "Opens NCBI dbSNP database in external window"),
        ("Variant Detail ClinVar External Reference", "variants", "low", "Click ClinVar link in variant modal", "Opens NCBI ClinVar database entry"),
        ("Variants Table Sort by rsID", "variants", "low", "Click rsID column header", "Table sorts variants numerically by rs number"),
        ("Variants Reset Filters Action", "variants", "medium", "Click 'Reset Filters' on variants page", "Clears mutation type and clinical significance filters"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(assoc_var_defs, start=141):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 6. Pathways & Drugs (SEL-176 - SEL-210) = 35
    pathway_drug_defs = [
        ("Pathways Catalog Page Initial Load", "pathways", "critical", "Navigate to /pathways catalog page", "Pathways list loads successfully"),
        ("Pathways Table Column Headers Check", "pathways", "high", "Verify columns on pathways page", "Columns: Pathway Name, Source, Category, Gene Count, Actions"),
        ("Pathways Search by Name 'DNA Repair'", "pathways", "high", "Type 'DNA Repair' in pathway search box", "Table displays homologous recombination and DNA repair pathways"),
        ("Pathways Search by Name 'Apoptosis'", "pathways", "high", "Type 'Apoptosis' in pathway search", "Table displays programmed cell death pathways"),
        ("Pathways Filter by Source 'KEGG'", "pathways", "medium", "Select 'KEGG' in source filter dropdown", "Table shows pathways curated from KEGG database"),
        ("Pathways Filter by Source 'Reactome'", "pathways", "medium", "Select 'Reactome' in source filter", "Table shows pathways curated from Reactome database"),
        ("Pathways Click Row to Open Detail View", "pathways", "high", "Click pathway row 'Cell Cycle Checkpoints'", "Navigates to pathway detail page"),
        ("Pathway Detail Title and Description Card", "pathways", "high", "Inspect pathway detail page overview", "Displays official title, biological description, and category"),
        ("Pathway Detail Associated Genes Chips", "pathways", "high", "Inspect associated genes list in pathway detail", "Displays interactive gene symbol badges for member genes"),
        ("Pathway Detail Click Member Gene Chip", "pathways", "medium", "Click on gene chip 'CDK1' inside pathway detail", "Navigates to /genes/CDK1 gene detail page"),
        ("Pathway Detail External Source Link", "pathways", "low", "Click external database link (KEGG/Reactome)", "Opens pathway entry in respective external repository"),
        ("Pathways Pagination Controls", "pathways", "medium", "Click Next page button on pathways catalog", "Loads next page of pathways"),
        ("Pathways Reset Filters Action", "pathways", "low", "Click 'Reset Filters' on pathways page", "All pathway filters cleared"),
        ("Drugs Catalog Page Initial Load", "drugs", "critical", "Navigate to /drugs catalog page", "Drugs catalog table loads with therapeutic agents"),
        ("Drugs Column Headers Verification", "drugs", "high", "Verify columns on drugs page", "Columns: Drug Name, Mechanism of Action, Target Gene, Clinical Phase, Status"),
        ("Drugs Search by Name 'Olaparib'", "drugs", "high", "Type 'Olaparib' in drug search input", "Table filters to Olaparib PARP inhibitor record"),
        ("Drugs Search by Name 'Imatinib'", "drugs", "high", "Type 'Imatinib' in drug search input", "Table filters to Imatinib tyrosine kinase inhibitor"),
        ("Drugs Filter by Phase 'Approved'", "drugs", "high", "Select 'FDA Approved' in clinical phase filter", "Table displays only approved commercial therapeutics"),
        ("Drugs Filter by Phase 'Phase III'", "drugs", "medium", "Select 'Phase III' in clinical phase filter", "Table displays drugs undergoing Phase 3 clinical trials"),
        ("Drugs Filter by Phase 'Phase II'", "drugs", "medium", "Select 'Phase II' in clinical phase filter", "Table displays Phase 2 investigational drugs"),
        ("Drugs Filter by Phase 'Phase I'", "drugs", "low", "Select 'Phase I' in clinical phase filter", "Table displays Phase 1 early trial drugs"),
        ("Drugs Filter by Action 'Inhibitor'", "drugs", "high", "Select 'Inhibitor' in mechanism filter", "Table shows enzyme and receptor inhibitors"),
        ("Drugs Filter by Action 'Agonist'", "drugs", "medium", "Select 'Agonist' in mechanism filter", "Table shows receptor agonists"),
        ("Drugs Filter by Action 'Antagonist'", "drugs", "medium", "Select 'Antagonist' in mechanism filter", "Table shows receptor antagonists"),
        ("Drugs Click Target Gene Chip Navigation", "drugs", "high", "Click target gene chip (e.g. EGFR) in drug row", "Navigates directly to /genes/EGFR detail view"),
        ("Drugs Detail Modal Overview", "drugs", "medium", "Click drug row to open detail modal", "Modal displays chemical name, indications, and target affinities"),
        ("Drugs Detail Indication List", "drugs", "medium", "Inspect clinical indications section in modal", "Lists approved and investigational disease indications"),
        ("Drugs External Reference to DrugBank", "drugs", "low", "Click DrugBank link in drug detail modal", "Opens DrugBank entry in new tab"),
        ("Drugs Table Sort by Drug Name", "drugs", "medium", "Click 'Drug Name' column header", "Drugs sorted alphabetically A-Z"),
        ("Drugs Table Sort by Clinical Phase", "drugs", "low", "Click 'Clinical Phase' column header", "Drugs sorted by approval maturity stage"),
        ("Drugs Reset Filters Action", "drugs", "medium", "Click 'Reset Filters' on drugs page", "Clears search, phase, and mechanism filter selections"),
        ("Drugs Empty Search State Handling", "drugs", "low", "Search for 'UnknownFakeMolecule'", "Displays 'No drugs found matching criteria'"),
        ("Drugs Catalog Mobile View Responsive Layout", "drugs", "medium", "Resize browser window to mobile width", "Drugs render in responsive summary cards"),
        ("Pathways Catalog Mobile Responsive Grid", "pathways", "medium", "Resize browser to 400px width on pathways page", "Pathways table switches to touch-friendly card list"),
        ("Pathway Detail Search Genes in Pathway", "pathways", "low", "Filter member genes input inside pathway detail", "Filters displayed gene chips matching typed letters"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(pathway_drug_defs, start=176):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 7. Publications & Global Search (SEL-211 - SEL-245) = 35
    pub_search_defs = [
        ("Publications Catalog Initial Load", "publications", "critical", "Navigate to /publications catalog page", "Publications list loads with scientific articles"),
        ("Publications Columns Verification", "publications", "high", "Verify table column headers", "Columns: Title, Journal, Year, PubMed ID, Linked Genes, Linked Diseases"),
        ("Publications Search by Title Keyword", "publications", "high", "Search publications for 'genomic landscape'", "Displays articles containing keyword in title"),
        ("Publications Search by PubMed ID 'PMID'", "publications", "high", "Enter specific PMID number in search", "Displays exact publication record matching PMID"),
        ("Publications Filter by Journal 'Nature'", "publications", "medium", "Select 'Nature' in journal filter dropdown", "Displays articles published in Nature portfolio"),
        ("Publications Filter by Journal 'Cell'", "publications", "medium", "Select 'Cell' in journal filter", "Displays articles published in Cell journal"),
        ("Publications Filter by Year '2023'", "publications", "medium", "Select year '2023' in publication year filter", "Displays articles published in year 2023"),
        ("Publications Filter by Year Range", "publications", "low", "Select year range 2020-2024", "Displays articles published between 2020 and 2024"),
        ("Publications Click Linked Gene Chip", "publications", "high", "Click linked gene badge on publication card", "Navigates to the corresponding gene detail page"),
        ("Publications Click Linked Disease Chip", "publications", "high", "Click linked disease badge on publication card", "Navigates to the corresponding disease detail page"),
        ("Publications External PubMed Link", "publications", "medium", "Click PubMed ID button on publication row", "Opens official NCBI PubMed article in external window"),
        ("Publications Abstract Toggle Expand", "publications", "medium", "Click 'View Abstract' button on publication card", "Card expands showing full scientific abstract text"),
        ("Publications Abstract Collapse Action", "publications", "low", "Click 'Hide Abstract' button", "Abstract collapses back to compact preview"),
        ("Publications Table Pagination Controls", "publications", "medium", "Click Next on publications pagination", "Loads next batch of literature records"),
        ("Publications Reset Filters Action", "publications", "low", "Click 'Reset Filters' on publications page", "All journal and year filters reset"),
        ("Global Search Input Open from Keyboard Shortcut", "search", "high", "Press 'Cmd+K' / 'Ctrl+K' anywhere in application", "Global search modal dialog opens with active focus"),
        ("Global Search Multi-Entity Query 'BRCA'", "search", "critical", "Enter 'BRCA' in global search modal", "Returns multi-category results: Genes, Diseases, Variants, Publications"),
        ("Global Search Filter by Type 'Gene'", "search", "high", "Click 'Genes' filter pill in global search", "Search results filter to show only gene matches"),
        ("Global Search Filter by Type 'Disease'", "search", "high", "Click 'Diseases' filter pill", "Search results filter to show only disease matches"),
        ("Global Search Filter by Type 'Variant'", "search", "high", "Click 'Variants' filter pill", "Search results filter to show only genetic variants"),
        ("Global Search Filter by Type 'Pathway'", "search", "medium", "Click 'Pathways' filter pill", "Search results filter to show only pathway matches"),
        ("Global Search Filter by Type 'Drug'", "search", "medium", "Click 'Drugs' filter pill", "Search results filter to show only drug target matches"),
        ("Global Search Filter by Type 'Publication'", "search", "medium", "Click 'Publications' filter pill", "Search results filter to show only literature results"),
        ("Global Search Result Highlight Tags", "search", "medium", "Inspect highlighted text in search snippet", "Matched search terms enclosed in highlight markup tag"),
        ("Global Search Arrow Key Navigation", "search", "medium", "Use Down Arrow key to cycle through search results", "Active highlight moves sequentially down results list"),
        ("Global Search Select Result via Enter Key", "search", "high", "Press Enter on highlighted search result", "Navigates directly to selected item's detail view"),
        ("Global Search Clear Query Button", "search", "low", "Click 'X' icon inside global search input", "Query text cleared and results list resets"),
        ("Global Search Close Modal via Escape Key", "search", "medium", "Press Escape key while search modal is open", "Search modal closes immediately returning focus to page"),
        ("Global Search Close Modal via Backdrop Click", "search", "medium", "Click semi-transparent backdrop outside modal", "Search modal closes"),
        ("Global Search Empty State for Unknown Keyword", "search", "medium", "Search for 'NonExistentBiomarkerXYZ'", "Displays 'No matching results found across database'"),
        ("Global Search Special Characters Handling", "search", "medium", "Enter query with punctuation '!@#$%^&*()'", "Query sanitized cleanly without crashing search UI"),
        ("Global Search Deep Link with URL Param ?q=", "search", "high", "Directly navigate to /search?q=TP53", "Page loads with query 'TP53' prefilled and executed"),
        ("Global Search Fallback Mode Notice", "search", "low", "Verify UI when search backend runs in SQL fallback", "Results display seamlessly without error banners"),
        ("Global Search History Persistence", "search", "low", "Re-open search modal after a query", "Recent searches list displays previously searched keywords"),
        ("Global Search Clear Search History", "search", "low", "Click 'Clear recent searches' button", "Saved search keywords removed from local storage"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(pub_search_defs, start=211):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 8. Analytics, AI Insights & Database Explorer (SEL-246 - SEL-275) = 30
    analytics_defs = [
        ("Analytics Page Initial Load", "analytics", "critical", "Navigate to /analytics overview page", "Dashboard renders with statistical cards and chart widgets"),
        ("Analytics Summary Metric - Total Genes Count", "analytics", "high", "Verify 'Total Genes' counter card", "Card displays non-zero numerical count matching database"),
        ("Analytics Summary Metric - Total Diseases Count", "analytics", "high", "Verify 'Total Diseases' counter card", "Card displays total count of curated diseases"),
        ("Analytics Summary Metric - Total Associations Count", "analytics", "high", "Verify 'Total Associations' metric", "Card displays total disease-gene pairs"),
        ("Analytics Summary Metric - Total Variants Count", "analytics", "high", "Verify 'Total Variants' counter card", "Card displays total genetic variants in system"),
        ("Analytics Summary Metric - Total Pathways Count", "analytics", "medium", "Verify 'Total Pathways' metric card", "Card displays total biological pathways recorded"),
        ("Chromosome Distribution Bar Chart Render", "analytics", "high", "Inspect Chromosome Distribution chart container", "Bar chart renders bars for Chromosomes 1 through 22, X, Y"),
        ("Chromosome Distribution Hover Tooltip", "analytics", "medium", "Hover mouse over Chr 1 bar in distribution chart", "Interactive tooltip displays exact gene count for Chr 1"),
        ("Pathogenicity Distribution Chart Render", "analytics", "high", "Inspect Evidence Level / Pathogenicity donut chart", "Donut chart renders slices for Level A, B, C, D evidence"),
        ("Pathogenicity Chart Legend Toggle", "analytics", "medium", "Click 'Level A' in chart legend", "Slice toggles visibility updating chart proportions"),
        ("Analytics Chart Refresh Button", "analytics", "low", "Click 'Refresh Data' button on analytics page", "Triggers re-fetch of /api/v1/stats updating all metric cards"),
        ("Analytics Export Chart as PNG", "analytics", "low", "Click camera/download icon on Plotly toolbar", "Chart image downloaded as PNG file to client"),
        ("Analytics Responsive Layout on Mobile", "analytics", "medium", "View analytics dashboard on 375px mobile viewport", "Metric cards and charts stack vertically without overflow"),
        ("AI Insights Network Graph Canvas Render", "ai-insights", "critical", "Navigate to /ai-insights network visualization", "Interactive D3/network graph canvas renders nodes and edges"),
        ("AI Insights Graph Node Selection", "ai-insights", "high", "Click on gene node in network visualization", "Sidebar displays gene metadata and connected disease links"),
        ("AI Insights Graph Zoom In / Zoom Out Controls", "ai-insights", "medium", "Click '+' and '-' zoom buttons on graph canvas", "Canvas zoom scale increases/decreases smoothly"),
        ("AI Insights Graph Reset View Button", "ai-insights", "low", "Click 'Reset View' button after panning", "Network graph centers back to initial viewport coordinate"),
        ("AI Insights Confidence Threshold Filter", "ai-insights", "high", "Drag confidence slider on AI insights page", "Edges with lower confidence filtered out of graph display"),
        ("AI Insights Search Node in Graph", "ai-insights", "medium", "Type gene symbol into graph node locator input", "Target node highlighted and camera pans to focus on it"),
        ("AI Insights Node Drag and Drop Interaction", "ai-insights", "low", "Click and drag node on force-directed graph", "Node relocates dynamically following physics simulation"),
        ("Database Explorer Page Initial Load", "database", "critical", "Navigate to /database explorer view", "Data tables browser loads showing database summary"),
        ("Database Explorer Table Selector Dropdown", "database", "high", "Switch table selector from 'Genes' to 'Diseases'", "Data preview table switches to disease database schema"),
        ("Database Explorer Schema Definition Tab", "database", "medium", "Click 'Schema' tab on database explorer", "Displays SQL schema column names, data types, and nullability"),
        ("Database Explorer Row Filter Input", "database", "medium", "Enter filter condition on database explorer table", "Table filters preview rows according to condition"),
        ("Database Explorer CSV Export Button", "database", "medium", "Click 'Export Table as CSV' button", "Browser downloads CSV file containing current table rows"),
        ("Database Explorer JSON Export Button", "database", "low", "Click 'Export Table as JSON' button", "Browser downloads JSON export file"),
        ("Favorites Page Initial Load", "favorites", "high", "Navigate to /favorites page while logged in", "Favorites page loads showing user's saved items"),
        ("Favorites Page Favorited Genes Tab", "favorites", "high", "Click 'Saved Genes' tab on favorites page", "Lists all genes favorited by current logged-in user"),
        ("Favorites Page Favorited Diseases Tab", "favorites", "high", "Click 'Saved Diseases' tab on favorites page", "Lists all diseases favorited by current user"),
        ("Favorites Page Remove Item from List", "favorites", "high", "Click trash/unfavorite icon on favorited item", "Item removed from favorites list and counter decrements"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(analytics_defs, start=246):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 9. Admin Dashboard, Security & Error Handling (SEL-276 - SEL-300) = 25
    admin_defs = [
        ("Admin Overview Page Access with Admin Role", "admin", "critical", "Login as Admin and navigate to /admin", "Admin dashboard renders summary cards and system settings"),
        ("Admin Overview Non-Admin Access Denial (403)", "admin", "critical", "Login as Researcher and navigate to /admin", "Access denied message 'Admin access required' displayed"),
        ("Admin Overview Metric Cards Verification", "admin", "high", "Inspect counts on /admin/overview", "Displays accurate counts for genes, diseases, variants, pathways, associations"),
        ("Admin Profile Update Valid Submission", "admin", "high", "Update Admin username and email on /admin/profile", "Success toast shown; profile updated in header"),
        ("Admin Profile Update Invalid Email Format", "admin", "medium", "Submit invalid email format on admin profile update", "Form validation highlights invalid email"),
        ("Admin Profile Update Blank Username", "admin", "medium", "Clear username field and submit profile update", "Validation error 'Username cannot be blank' displayed"),
        ("Admin Ingestion Upload Modal Open", "admin", "high", "Click 'Upload Dataset' button in admin panel", "Dataset upload modal dialog opens"),
        ("Admin Ingestion Upload Valid CSV File", "admin", "critical", "Select valid genes_dataset.csv and click Upload", "Upload succeeds with ingestion confirmation report"),
        ("Admin Ingestion Upload Invalid File Extension (.txt)", "admin", "medium", "Select .txt file in upload dialog", "Validation error 'Only CSV files supported' displayed"),
        ("Admin Ingestion Upload File Size Exceeded", "admin", "medium", "Attempt to upload file exceeding max file size limit", "Error notification 'File size exceeds maximum allowed limit'"),
        ("Admin Ingestion Empty File Upload", "admin", "low", "Attempt to upload 0-byte CSV file", "Error notification 'Uploaded file is empty' displayed"),
        ("Session Token Tampering Handling", "security", "high", "Modify JWT token payload in localStorage to invalid string", "Next API call fails; user safely logged out and redirected to signin"),
        ("XSS Payload in Search Input Sanitization", "security", "high", "Enter '<script>alert(1)</script>' in search input", "Input rendered as sanitized text without script execution"),
        ("SQL Injection Characters in URL Parameters", "security", "high", "Navigate to /genes?chromosome=1'%20OR%20'1'='1", "Application safely returns 400/422 or empty list without SQL error"),
        ("Cross-Origin Request Block Verification", "security", "medium", "Simulate fetch from unauthorized origin in console", "CORS policy blocks unauthorized cross-origin request"),
        ("CSRF Cookie / Header Validation", "security", "medium", "Inspect state-changing POST requests", "Authorization header or CSRF token validated on sensitive mutations"),
        ("Network Error Toast on Server Disconnect", "error-handling", "high", "Simulate offline network condition during search", "Toast notification 'Network error: unable to reach server' displayed"),
        ("Server 500 Internal Error Graceful Handling", "error-handling", "medium", "Simulate server 500 response", "Generic friendly error message shown without exposing stack traces"),
        ("Form Submit Button Disable on Click", "ui", "medium", "Click submit button on registration form", "Button disabled with loading spinner to prevent double submission"),
        ("Browser Back Button After Logout", "browser", "high", "Log out then click browser back button", "Protected page content not displayed from cache; redirected to signin"),
        ("Browser Refresh on Form Input Retention", "browser", "low", "Refresh page while editing search filters", "Query parameters in URL restore search filter state on reload"),
        ("Tab Focus Accessibility Traversal", "accessibility", "medium", "Use Tab key to traverse header navigation items", "Focus outline visible on every active interactive element"),
        ("ARIA Labels on Icon Buttons", "accessibility", "low", "Inspect heart, theme switch, and close icon buttons", "All icon buttons have descriptive aria-label attributes"),
        ("Screen Reader Heading Hierarchy", "accessibility", "low", "Audit page heading structure with axe/lighthouse", "Single h1 heading per page followed by sequential h2/h3 elements"),
        ("Color Contrast Ratio Conformance", "accessibility", "low", "Audit text contrast against dark and light backgrounds", "All text elements meet WCAG AA contrast ratio threshold of 4.5:1"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(admin_defs, start=276):
        cases.append({"id": f"SEL-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    return cases


def generate_appium_cases():
    cases = []
    
    # 1. Installation, Launch & Lifecycle (APP-001 - APP-035) = 35
    app_defs = [
        ("Clean App Installation from APK", "installation", "critical", "Install debug APK onto Android emulator via adb/Appium", "App installed successfully with package com.romcom.diseasegenemap"),
        ("App Cold Launch from Launcher", "lifecycle", "critical", "Launch app from Android app drawer icon", "App launches and displays splash screen"),
        ("Splash Screen Display Duration", "lifecycle", "high", "Verify splash screen appears with app logo", "Splash screen dismisses cleanly transitioning to home/signin"),
        ("Default Landing Screen on First Launch", "lifecycle", "high", "Inspect landing screen on fresh install without saved session", "Home landing or signin screen displayed"),
        ("App Permissions - Internet Access", "permissions", "critical", "Verify Android Manifest INTERNET permission granted", "App initiates network API requests successfully"),
        ("App Background and Resume (10 Seconds)", "lifecycle", "high", "Send app to background for 10s then bring to foreground", "App resumes seamlessly without crash or reload loss"),
        ("App Background and Resume (60 Seconds)", "lifecycle", "medium", "Send app to background for 60s and resume", "App session state preserved intact"),
        ("Device Back Button from Sub-Screen", "lifecycle", "high", "Navigate to Gene detail and press Android hardware back button", "Returns cleanly to previous genes list screen"),
        ("Device Back Button from Root Screen", "lifecycle", "medium", "Press Android back button from root home screen", "App exits or prompts confirmation dialog"),
        ("Device Home Button Interaction", "lifecycle", "medium", "Press device home button while browsing", "App minimizes smoothly to Android launcher"),
        ("App Switcher / Recent Apps Card", "lifecycle", "low", "Open Android recent apps overview", "App card displayed with proper app name 'diseaseGene'"),
        ("App Relaunch from Recent Apps", "lifecycle", "medium", "Tap app card in recent apps screen", "App resumes immediately at last viewed screen"),
        ("Device Screen Rotation to Landscape", "lifecycle", "high", "Rotate emulator to LANDSCAPE orientation", "Layout reorganizes to landscape without clipping or crash"),
        ("Device Screen Rotation Back to Portrait", "lifecycle", "high", "Rotate emulator back to PORTRAIT orientation", "Layout restores portrait orientation cleanly"),
        ("Low Memory Trim Event Simulation", "lifecycle", "medium", "Trigger low memory trim event via adb command", "App recovers gracefully without memory crash"),
        ("App Cold Restart with Saved Session", "lifecycle", "high", "Force stop app and relaunch after user login", "User remains logged in via stored credentials/token"),
        ("App Launch After Device Reboot", "lifecycle", "medium", "Restart Android emulator and launch app", "App boots and handles cold storage initialization"),
        ("Capacitor Bridge Initialization Check", "lifecycle", "critical", "Verify Capacitor native bridge loaded", "Capacitor runtime ready and native plugins operational"),
        ("Android Status Bar Theming", "ui", "low", "Inspect Android top status bar color", "Status bar matches application dark background theme #050507"),
        ("Android Navigation Bar Theming", "ui", "low", "Inspect Android bottom system navigation bar", "System navigation bar blends seamlessly with app footer"),
        ("Splash Screen Spinner Visibility", "ui", "low", "Inspect spinner during initial cold boot", "Spinner displayed with theme color #00f5d4"),
        ("App Version Verification in Settings", "lifecycle", "low", "Open about section in mobile settings", "Displays version matching Capacitor config 1.0.0"),
        ("Multiple Rapid Launches Stress", "lifecycle", "medium", "Launch and kill app 5 times in quick succession", "App starts reliably on every launch attempt"),
        ("Hardware Volume Keys Interaction", "device", "low", "Press device volume up/down keys while in app", "Volume slider displays without interfering with UI"),
        ("Device Power Button Lock / Unlock", "device", "medium", "Lock emulator screen and unlock after 5 seconds", "App display wakes up on last viewed screen"),
        ("App Window Focus Loss on System Dialog", "lifecycle", "low", "Trigger system alert dialog over app", "App pauses rendering and resumes on dialog dismissal"),
        ("Multi-Window / Split Screen Mode", "lifecycle", "low", "Enter Android split-screen mode with another app", "App resizes viewport and adapts responsive mobile layout"),
        ("Font Size Scaling Accessibility", "accessibility", "medium", "Increase Android system font size to 'Largest'", "Text scales legibly without overlapping UI controls"),
        ("Display Size Scaling Accessibility", "accessibility", "medium", "Increase Android display density setting", "Buttons and touch targets scale appropriately"),
        ("TalkBack Screen Reader Node Descriptions", "accessibility", "low", "Enable TalkBack and inspect main navigation items", "Accessibility labels announced for tabs and buttons"),
        ("App Kill and Restore Last Active Tab", "lifecycle", "medium", "Kill app process from task manager and restart", "App restores cleanly to default or saved active route"),
        ("Dark Mode System Theme Sync", "ui", "medium", "Toggle Android system Dark Theme setting", "App conforms to system theme mode preferences"),
        ("Offline Launch Handling", "network", "high", "Launch app while emulator in Airplane mode", "Displays friendly offline banner without crashing"),
        ("Network Restoration from Offline", "network", "high", "Disable Airplane mode while app running", "App detects online connection and reloads content"),
        ("App Uninstallation Cleanliness", "installation", "low", "Uninstall app from emulator via adb", "App package removed cleanly from device"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(app_defs, start=1):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 2. Mobile Authentication & Account (APP-036 - APP-075) = 40
    mobile_auth = [
        ("Mobile Login Screen Elements Check", "auth", "critical", "Open signin screen on mobile", "Displays username input, password input, signin button, forgot links"),
        ("Mobile Keyboard Appearance on Input Focus", "auth", "high", "Tap username input field", "Android soft keyboard appears automatically"),
        ("Mobile Keyboard 'Next' Key Action", "auth", "medium", "Press 'Next' action key on keyboard while in username", "Keyboard focus moves directly to password input"),
        ("Mobile Keyboard 'Done' Key Action", "auth", "medium", "Press 'Done' / Enter key in password field", "Triggers login form submission"),
        ("Mobile Password Obscurity Masking", "auth", "high", "Type password in password field", "Characters masked with bullets by default"),
        ("Mobile Password Reveal Toggle Tap", "auth", "low", "Tap eye icon inside mobile password input", "Password characters revealed in plain text"),
        ("Mobile Valid Researcher Login", "auth", "critical", "Enter valid researcher credentials and tap Sign In", "Keyboard dismisses, loader displays, and user logged in"),
        ("Mobile Valid Admin Login", "auth", "critical", "Enter valid admin credentials and tap Sign In", "User logged in with admin dashboard accessible"),
        ("Mobile Login Invalid Password Toast", "auth", "high", "Enter incorrect password and tap Sign In", "Android toast/banner shows 'Incorrect username or password'"),
        ("Mobile Login Empty Fields Validation", "auth", "medium", "Tap Sign In with empty fields", "Validation error text appears beneath empty inputs"),
        ("Mobile Login Keyboard Dismiss on Outside Tap", "auth", "medium", "Tap outside input field onto screen background", "Soft keyboard dismisses cleanly"),
        ("Mobile Logout Flow via Drawer/Settings", "auth", "critical", "Open mobile user menu and tap 'Logout'", "Session cleared, user returned to signin screen"),
        ("Mobile Registration Screen Navigation", "auth", "high", "Tap 'Don't have an account? Sign Up' link", "Navigates to mobile registration screen"),
        ("Mobile Registration Form Inputs", "auth", "high", "Verify registration form fields", "Inputs: Username, Email, Password, Confirm Password"),
        ("Mobile Registration Valid Submission", "auth", "critical", "Fill valid details and submit registration", "Account created; confirmation toast displayed"),
        ("Mobile Registration Duplicate Username", "auth", "high", "Register with existing username", "Error toast 'Username or email already registered' displayed"),
        ("Mobile Registration Password Strength Indicator", "auth", "medium", "Type weak password in registration input", "Strength meter shows 'Weak' with requirements checklist"),
        ("Mobile Forgot Password Screen Navigation", "auth", "high", "Tap 'Forgot Password?' link on signin screen", "Navigates to mobile forgot password view"),
        ("Mobile Forgot Password Email Submission", "auth", "high", "Enter valid email and tap 'Send OTP'", "Toast displays 'If that email exists, a reset code has been sent'"),
        ("Mobile OTP Input Screen Format", "auth", "high", "Inspect reset password screen with OTP input", "Displays 6-digit verification code input and new password field"),
        ("Mobile OTP Numeric Keyboard Trigger", "auth", "medium", "Tap OTP verification code input field", "Android numeric keypad opens instead of full keyboard"),
        ("Mobile Reset Password Valid OTP Submission", "auth", "critical", "Enter email, valid 6-digit OTP, and new password", "Password reset successfully; user redirected to signin"),
        ("Mobile Reset Password Invalid OTP Handling", "auth", "high", "Enter incorrect OTP code and submit", "Error banner shows 'Invalid or expired OTP'"),
        ("Mobile Session Persistence Across App Restarts", "auth", "critical", "Restart app after login without logging out", "App opens directly into authenticated state"),
        ("Mobile Auth Token Expiry Detection", "auth", "high", "Simulate expired token in mobile storage", "App redirects to signin with session expired message"),
        ("Mobile Register with Special Chars in Username", "auth", "low", "Enter username with spaces or illegal characters", "Validation flags invalid characters"),
        ("Mobile Login Button Loading State", "auth", "medium", "Tap Sign In button during slow network", "Button shows spinner and disabled state to prevent duplicate taps"),
        ("Mobile Forgot Username Screen", "auth", "low", "Navigate to /forgot-username screen on mobile", "Displays email input for username recovery lookup"),
        ("Mobile Clear Stuck User Cleanup Action", "auth", "low", "Trigger clear-stuck-user API call from mobile debug tools", "Stuck user record deleted successfully"),
        ("Mobile Biometric / Fingerprint Prompt Placeholder", "auth", "low", "Inspect biometric login option if enabled", "Biometric option handled gracefully"),
        ("Mobile Profile Screen Display", "auth", "high", "Navigate to profile tab on mobile", "Displays user username, email address, and role badge"),
        ("Mobile Profile Edit Username and Email", "auth", "medium", "Update username and tap Save on mobile", "Profile updated with confirmation snackbar"),
        ("Mobile Admin Profile Guard on Mobile", "auth", "high", "Attempt to access admin panel as Researcher on mobile", "Access forbidden banner displayed"),
        ("Mobile Password Change from Profile", "auth", "medium", "Submit password update form from profile settings", "Password updated successfully"),
        ("Mobile Remember Credentials Checkbox", "auth", "low", "Toggle 'Remember Me' switch on mobile signin", "Switch toggles and persists preference"),
        ("Mobile Quick Signin Form Reset", "auth", "low", "Clear form button clears all inputs", "Username and password inputs emptied"),
        ("Mobile Input Auto-Capitalize Disabled for Username", "auth", "low", "Inspect auto-capitalize attribute on username", "Input starts in lowercase without auto-capitalizing"),
        ("Mobile Email Input Type Email Keyboard", "auth", "low", "Tap email input field on mobile", "Keyboard includes '@' and '.' shortcut keys"),
        ("Mobile Password Input Secure Type", "auth", "medium", "Inspect Android inputType attribute on password", "Input type set to textPassword"),
        ("Mobile Session Logout Confirmation Dialog", "auth", "medium", "Tap logout button in settings", "Confirmation dialog 'Are you sure you want to log out?' displayed"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_auth, start=36):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 3. Mobile Navigation, Gestures & Layout (APP-076 - APP-115) = 40
    mobile_nav = [
        ("Mobile Bottom Navigation Bar Presence", "navigation", "critical", "Inspect bottom navigation bar on mobile screen", "Bottom bar displays tabs: Home, Genes, Diseases, Search, More"),
        ("Mobile Bottom Tab Switch - Home", "navigation", "high", "Tap 'Home' tab on bottom navigation bar", "Navigates to home screen with Home icon active"),
        ("Mobile Bottom Tab Switch - Genes", "navigation", "high", "Tap 'Genes' tab on bottom navigation bar", "Navigates to Genes catalog screen"),
        ("Mobile Bottom Tab Switch - Diseases", "navigation", "high", "Tap 'Diseases' tab on bottom navigation bar", "Navigates to Diseases catalog screen"),
        ("Mobile Bottom Tab Switch - Search", "navigation", "high", "Tap 'Search' tab on bottom navigation bar", "Navigates to dedicated Search screen"),
        ("Mobile Bottom Tab Switch - More / Menu", "navigation", "high", "Tap 'More' tab on bottom navigation bar", "Opens more menu with Pathways, Variants, Analytics, Admin"),
        ("Mobile Drawer Swipe Right Gesture", "gestures", "high", "Swipe finger from left screen edge towards right", "Navigation drawer slides open smoothly"),
        ("Mobile Drawer Swipe Left to Close", "gestures", "high", "Swipe drawer towards left screen edge", "Navigation drawer closes smoothly"),
        ("Mobile Pull-to-Refresh on Genes Feed", "gestures", "high", "Pull down from top of genes list and release", "Refresh spinner activates and latest gene data reloaded"),
        ("Mobile Pull-to-Refresh on Diseases Feed", "gestures", "high", "Pull down from top of diseases list", "Refresh spinner activates and reloads diseases"),
        ("Mobile Vertical Fling Scrolling", "gestures", "medium", "Perform rapid vertical swipe gesture down list", "List scrolls smoothly with inertial deceleration"),
        ("Mobile Scroll to Top Floating Button", "gestures", "medium", "Scroll down 50 items and tap 'Scroll to Top' FAB", "List scrolls smoothly back to top item"),
        ("Mobile Horizontal Swipe on Category Chips", "gestures", "medium", "Swipe horizontally across filter category pill list", "Chips scroll horizontally revealing additional categories"),
        ("Mobile Tap Target Size Compliance (min 48dp)", "ui", "medium", "Measure touch bounds of buttons and icons", "All interactive touch targets have minimum 48x48dp dimensions"),
        ("Mobile Header Bar Brand and Notification", "ui", "low", "Inspect top mobile app header", "Displays app title 'diseaseGene' and theme toggle"),
        ("Mobile Theme Switcher in Header", "ui", "medium", "Tap sun/moon theme icon in mobile top bar", "App color palette toggles between dark and light"),
        ("Mobile Breadcrumb Bar on Detail Screens", "navigation", "medium", "Navigate to sub-detail screen on mobile", "Top bar shows back arrow button '<' and screen title"),
        ("Mobile Header Back Arrow Tap", "navigation", "high", "Tap '<' back arrow in top bar", "Navigates back to parent screen"),
        ("Mobile Double Tap Zoom on Network Chart", "gestures", "low", "Double-tap on AI Insights network graph canvas", "Graph canvas zooms in by 1.5x"),
        ("Mobile Pinch-to-Zoom on Network Canvas", "gestures", "low", "Perform two-finger pinch gesture on graph", "Graph scales dynamically following finger distance"),
        ("Mobile Long-Press on Gene Card", "gestures", "medium", "Press and hold gene card for 800ms", "Context action sheet opens with 'Favorite', 'Share', 'Copy'"),
        ("Mobile Bottom Sheet Filter Dialog", "ui", "high", "Tap 'Filter' button on catalog screen", "Bottom sheet slides up from bottom of screen"),
        ("Mobile Bottom Sheet Drag Down to Dismiss", "gestures", "medium", "Drag bottom sheet handle downwards", "Bottom sheet dismisses returning to main list"),
        ("Mobile Toast Notification Auto-Dismiss", "ui", "low", "Trigger toast notification message", "Toast displays and automatically fades after 3 seconds"),
        ("Mobile Action Snackbar with 'Undo'", "ui", "low", "Unfavorite item from list", "Snackbar shows 'Removed from favorites' with 'Undo' action"),
        ("Mobile Responsive Card Padding", "ui", "low", "Inspect card margin and padding on 360dp screen", "Content margins maintain 16dp spacing without cutoff"),
        ("Mobile Floating Action Button (FAB)", "ui", "low", "Inspect FAB button on explorer screen", "FAB floats above list in bottom-right corner"),
        ("Mobile Tab Bar Hiding on Scroll Down", "ui", "low", "Scroll downwards continuously on long list", "Bottom bar collapses to maximize screen viewing area"),
        ("Mobile Tab Bar Reveal on Scroll Up", "ui", "low", "Scroll upwards slightly while on list", "Bottom bar slides back into view"),
        ("Mobile Search Bar Floating Header", "ui", "medium", "Inspect search bar position on mobile search screen", "Search bar pinned below status bar with clear visibility"),
        ("Mobile Haptic Feedback on Important Taps", "gestures", "low", "Tap favorite heart button", "Device triggers brief subtle haptic vibration"),
        ("Mobile Swipe-to-Dismiss Favorite Item", "gestures", "medium", "Swipe item horizontally to the left in favorites list", "Item removed from list with red trash background"),
        ("Mobile Dialog Alert Confirmation", "ui", "medium", "Trigger delete/reset action dialog", "Modal alert dialog renders centered on mobile display"),
        ("Mobile Dialog Cancel Button", "ui", "medium", "Tap 'Cancel' in confirmation dialog", "Dialog closes without executing destructive action"),
        ("Mobile Screen Title Truncation Prevention", "ui", "low", "View screen with long title on small screen", "Title truncates with ellipsis (...) rather than overflowing"),
        ("Mobile Notch / Safe Area Inset Handling", "ui", "medium", "Inspect app layout on device with display cutout/notch", "Header content respects top safe area insets"),
        ("Mobile Gesture Navigation Compatibility", "navigation", "medium", "Use Android system side-swipe back gesture", "System back gesture navigates back cleanly in app"),
        ("Mobile Screen Reader Focus Traversal Order", "accessibility", "low", "Swipe right in TalkBack mode", "Focus moves sequentially from header to content to footer"),
        ("Mobile High Contrast Mode Rendering", "accessibility", "low", "Enable Android high contrast text mode", "Text borders and outlines render sharply"),
        ("Mobile Loading Shimmer Effect", "ui", "medium", "Inspect card loading animation during network request", "Shimmer gradient animates across placeholder cards"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_nav, start=76):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 4. Mobile Genes, Diseases & Search (APP-116 - APP-165) = 50
    mobile_data = [
        ("Mobile Genes List Initial Rendering", "genes", "critical", "Open Genes tab on mobile app", "Genes list displays cards with gene symbol and name"),
        ("Mobile Genes Infinite Scroll Loading", "genes", "high", "Scroll to bottom of genes list", "Loading indicator appears and loads next batch of genes"),
        ("Mobile Genes Search by Symbol 'BRCA1'", "genes", "critical", "Type 'BRCA1' in mobile genes search bar", "List filters immediately to BRCA1 record card"),
        ("Mobile Genes Chromosome Filter Bottom Sheet", "genes", "high", "Tap 'Chromosome' filter pill on mobile", "Bottom sheet opens with grid of Chr 1..22, X, Y buttons"),
        ("Mobile Genes Filter Selection 'Chr 17'", "genes", "high", "Select 'Chr 17' in bottom sheet and tap 'Apply'", "Genes list updates showing only Chr 17 genes"),
        ("Mobile Genes Clear Chromosome Filter", "genes", "medium", "Tap 'Clear' in filter bottom sheet", "Filter cleared and all chromosomes shown"),
        ("Mobile Gene Card Tap to Open Detail", "genes", "critical", "Tap on 'BRCA1' card in genes list", "Navigates to mobile Gene detail view"),
        ("Mobile Gene Detail Header and Symbol", "genes", "high", "Inspect gene detail screen on mobile", "Displays large gene symbol, official name, and tags"),
        ("Mobile Gene Detail Genomic Coordinates Card", "genes", "medium", "Inspect coordinates section on mobile", "Displays Chromosome, Start/End positions in mobile card"),
        ("Mobile Gene Detail Function Section Accordion", "genes", "medium", "Tap 'Molecular Function' accordion section", "Accordion expands showing gene functional summary"),
        ("Mobile Gene Detail Protein Information Card", "genes", "medium", "Inspect protein section on mobile detail screen", "Displays protein name, length, and UniProt badge"),
        ("Mobile Gene Detail Favorite Heart Tap", "genes", "high", "Tap heart icon in top bar of gene detail", "Heart icon fills red with confirmation toast"),
        ("Mobile Gene Detail Unfavorite Tap", "genes", "high", "Tap filled heart icon again to unfavorite", "Heart un-fills with 'Removed from favorites' toast"),
        ("Mobile Gene Detail Share Button", "genes", "low", "Tap share icon in mobile top bar", "Android native share sheet opens with gene summary link"),
        ("Mobile Gene Detail Associated Diseases List", "genes", "high", "Scroll to 'Associated Diseases' on mobile gene detail", "Displays scrollable cards of linked diseases"),
        ("Mobile Gene Detail Tap Associated Disease", "genes", "high", "Tap on linked disease card 'Breast Cancer'", "Navigates directly to Disease detail screen"),
        ("Mobile Gene Detail Associated Variants Carousel", "genes", "medium", "Inspect variants section on mobile gene detail", "Displays horizontal swipeable carousel of variants"),
        ("Mobile Gene Detail Associated Pathways List", "genes", "medium", "Inspect pathways chips on mobile gene detail", "Displays pathway chips for DNA repair pathways"),
        ("Mobile Diseases List Initial Load", "diseases", "critical", "Open Diseases tab on mobile", "Diseases list renders with disease name cards"),
        ("Mobile Diseases Infinite Scroll", "diseases", "high", "Scroll to bottom of mobile diseases list", "Loads next batch of disease records"),
        ("Mobile Diseases Search by Name 'Diabetes'", "diseases", "critical", "Type 'Diabetes' in mobile disease search", "List filters to diabetes related conditions"),
        ("Mobile Diseases Category Filter Bottom Sheet", "diseases", "high", "Tap 'Category' filter pill", "Bottom sheet opens with Oncology, Neurology, Cardiology, etc."),
        ("Mobile Diseases Filter Selection 'Oncology'", "diseases", "high", "Select 'Oncology' and tap Apply", "List updates showing cancer diseases"),
        ("Mobile Disease Card Tap to Open Detail", "diseases", "critical", "Tap on disease card 'Alzheimer's Disease'", "Navigates to Disease detail screen on mobile"),
        ("Mobile Disease Detail Clinical Overview", "diseases", "high", "Inspect overview section on mobile disease detail", "Displays clinical etiology and ICD-10 code badge"),
        ("Mobile Disease Detail OMIM External Link", "diseases", "low", "Tap OMIM external link button", "Opens OMIM website in Chrome Custom Tab"),
        ("Mobile Disease Detail Favorite Heart Toggle", "diseases", "high", "Tap favorite icon on disease detail screen", "Disease added to favorites with confirmation"),
        ("Mobile Disease Detail Associated Genes Cards", "diseases", "high", "Scroll to linked genes section in disease detail", "Displays associated gene cards with confidence badges"),
        ("Mobile Disease Detail Tap Linked Gene", "diseases", "high", "Tap linked gene card 'APOE'", "Navigates directly to /genes/APOE screen"),
        ("Mobile Disease Detail Therapeutic Drugs List", "diseases", "medium", "Inspect drug treatments section on disease screen", "Displays approved drugs and investigational therapies"),
        ("Mobile Dedicated Search Tab Initial State", "search", "critical", "Open dedicated Search tab from bottom nav", "Displays search bar, recent searches, and entity type pills"),
        ("Mobile Search Auto-Focus Behavior", "search", "medium", "Tap search tab", "Search input auto-focuses and keyboard opens"),
        ("Mobile Search Multi-Entity Query 'TP53'", "search", "critical", "Type 'TP53' in mobile search input", "Returns combined results: Genes, Diseases, Variants"),
        ("Mobile Search Type Filter Pill 'Genes'", "search", "high", "Tap 'Genes' filter pill on mobile search", "Results filter to display only gene matches"),
        ("Mobile Search Type Filter Pill 'Diseases'", "search", "high", "Tap 'Diseases' filter pill", "Results filter to display only disease matches"),
        ("Mobile Search Type Filter Pill 'Variants'", "search", "medium", "Tap 'Variants' filter pill", "Results filter to display only variant matches"),
        ("Mobile Search Type Filter Pill 'Pathways'", "search", "medium", "Tap 'Pathways' filter pill", "Results filter to display only pathway matches"),
        ("Mobile Search Type Filter Pill 'Drugs'", "search", "medium", "Tap 'Drugs' filter pill", "Results filter to display only drug matches"),
        ("Mobile Search Result Item Tap Navigation", "search", "high", "Tap on search result card in list", "Navigates directly to selected item's mobile detail view"),
        ("Mobile Search Clear Button 'X' Tap", "search", "low", "Tap 'X' icon inside mobile search input", "Search text cleared and keyboard remains open"),
        ("Mobile Search Recent Searches Chip Tap", "search", "low", "Tap saved recent search chip 'BRCA1'", "Fills search input and executes query immediately"),
        ("Mobile Search Clear Recent History", "search", "low", "Tap 'Clear History' link in search tab", "All recent search chips removed from screen"),
        ("Mobile Search Empty Result Illustration", "search", "medium", "Search for 'UnknownBiomarker9999'", "Displays friendly empty state illustration with retry advice"),
        ("Mobile Search Special Characters Input", "search", "medium", "Enter punctuation and emoji in search input", "App handles input gracefully without crashing"),
        ("Mobile Search Offline Error Banner", "search", "high", "Perform search while device offline", "Displays banner 'Search requires internet connection'"),
        ("Mobile Search Debouncing Behavior", "search", "medium", "Type characters rapidly in search bar", "App debounces requests by 300ms before sending query"),
        ("Mobile Search Voice Input Button Presence", "search", "low", "Inspect mic icon in mobile search input", "Mic icon present for voice search integration"),
        ("Mobile Search Results Count Summary", "search", "low", "Inspect header above search results list", "Displays summary text 'Found 14 matching results'"),
        ("Mobile Search Result Highlight Styling", "search", "low", "Inspect matched text snippet in search card", "Matched query words highlighted in theme color"),
        ("Mobile Search Back Button Keyboard Dismissal", "search", "medium", "Press back button while search keyboard is open", "Dismisses keyboard first while remaining on search screen"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_data, start=116):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 5. Mobile Associations, Variants & Pathways (APP-166 - APP-205) = 40
    mobile_modules = [
        ("Mobile Associations Screen Initial Load", "associations", "critical", "Navigate to Associations screen on mobile", "Displays association cards with gene-disease pairs"),
        ("Mobile Associations Confidence Score Badge", "associations", "high", "Inspect confidence badge on association card", "Displays confidence score pill with color coding"),
        ("Mobile Associations Evidence Level Filter", "associations", "high", "Tap 'Evidence Level' filter on mobile", "Selects Level A/B/C/D evidence levels"),
        ("Mobile Associations Filter Level A Only", "associations", "high", "Filter associations by Level A on mobile", "Displays only high-confidence Level A associations"),
        ("Mobile Associations Score Slider Control", "associations", "medium", "Adjust score threshold slider in filter sheet", "Filters associations by minimum confidence threshold"),
        ("Mobile Associations Tap Gene Chip Navigation", "associations", "medium", "Tap gene symbol on association card", "Opens gene detail screen"),
        ("Mobile Associations Tap Disease Chip Navigation", "associations", "medium", "Tap disease name on association card", "Opens disease detail screen"),
        ("Mobile Associations Infinite Scrolling", "associations", "medium", "Scroll to bottom of mobile associations list", "Loads next page of association records"),
        ("Mobile Variants Screen Initial Load", "variants", "critical", "Navigate to Variants screen on mobile", "Displays variant cards with rsID and consequence"),
        ("Mobile Variants Filter by Clinical Significance", "variants", "high", "Tap 'Clinical Significance' filter pill", "Opens bottom sheet with Pathogenic, VUS, Benign"),
        ("Mobile Variants Filter 'Pathogenic' Selection", "variants", "critical", "Select 'Pathogenic' filter option", "Displays only pathogenic variants with red badge"),
        ("Mobile Variants Filter 'VUS' Selection", "variants", "medium", "Select 'VUS' filter option", "Displays variants of uncertain significance"),
        ("Mobile Variants Filter 'Benign' Selection", "variants", "medium", "Select 'Benign' filter option", "Displays benign variants with green badge"),
        ("Mobile Variants Search by rsID", "variants", "high", "Enter 'rs28897700' in variants search input", "Filters to matching rsID variant card"),
        ("Mobile Variant Card Tap to Open Modal", "variants", "high", "Tap variant card in list", "Bottom sheet modal opens with detailed HGVS annotations"),
        ("Mobile Variant Modal HGVS Coding Details", "variants", "medium", "Inspect HGVS c. notation in modal", "Displays coding DNA change format correctly"),
        ("Mobile Variant Modal HGVS Protein Details", "variants", "medium", "Inspect HGVS p. notation in modal", "Displays protein change format correctly"),
        ("Mobile Variant Modal External dbSNP Link", "variants", "low", "Tap dbSNP link in variant modal", "Opens dbSNP record in browser tab"),
        ("Mobile Variant Modal Dismiss via Drag", "variants", "medium", "Drag variant modal sheet downwards", "Modal dismisses smoothly"),
        ("Mobile Pathways Screen Initial Load", "pathways", "critical", "Navigate to Pathways screen on mobile", "Displays biological pathways catalog cards"),
        ("Mobile Pathways Search by Name", "pathways", "high", "Search 'DNA Repair' in pathways search", "Displays DNA repair related pathways"),
        ("Mobile Pathways Source Filter 'KEGG'", "pathways", "medium", "Filter pathways by 'KEGG' database", "Displays only KEGG pathway cards"),
        ("Mobile Pathways Source Filter 'Reactome'", "pathways", "medium", "Filter pathways by 'Reactome' database", "Displays only Reactome pathway cards"),
        ("Mobile Pathway Card Tap to Open Detail", "pathways", "high", "Tap on pathway card in mobile list", "Navigates to pathway detail view"),
        ("Mobile Pathway Detail Overview Card", "pathways", "medium", "Inspect description in mobile pathway detail", "Displays pathway biological description"),
        ("Mobile Pathway Detail Member Genes Chips", "pathways", "high", "Inspect member genes chips in pathway detail", "Displays interactive gene symbols"),
        ("Mobile Pathway Detail Tap Member Gene", "pathways", "medium", "Tap member gene chip 'ATM'", "Navigates to /genes/ATM detail screen"),
        ("Mobile Drugs Catalog Initial Load", "drugs", "critical", "Navigate to Drugs screen on mobile", "Displays therapeutic drugs cards"),
        ("Mobile Drugs Search by Molecule Name", "drugs", "high", "Search 'Olaparib' on mobile drugs screen", "Displays Olaparib drug card with target info"),
        ("Mobile Drugs Filter by Phase 'Approved'", "drugs", "high", "Filter drugs by 'Approved' clinical phase", "Displays FDA approved drugs"),
        ("Mobile Drugs Filter by Phase 'Phase III'", "drugs", "medium", "Filter drugs by 'Phase III'", "Displays Phase 3 investigational drugs"),
        ("Mobile Drugs Filter by Action 'Inhibitor'", "drugs", "medium", "Filter drugs by mechanism 'Inhibitor'", "Displays enzyme inhibitor therapeutics"),
        ("Mobile Drug Card Tap to Open Detail", "drugs", "high", "Tap on drug card in mobile list", "Opens drug detail sheet with indications and targets"),
        ("Mobile Drug Detail Target Gene Tap", "drugs", "medium", "Tap target gene chip in drug detail", "Navigates to target gene screen"),
        ("Mobile Publications Catalog Initial Load", "publications", "critical", "Navigate to Publications screen on mobile", "Displays literature citation cards"),
        ("Mobile Publications Search by Title", "publications", "high", "Search publications by title keyword", "Displays matching scientific papers"),
        ("Mobile Publications Tap PubMed ID Button", "publications", "medium", "Tap PubMed ID button on publication card", "Opens PubMed article in external browser"),
        ("Mobile Publications Abstract Expand Tap", "publications", "low", "Tap 'Read Abstract' link on mobile card", "Card expands displaying scientific abstract"),
        ("Mobile Publications Year Filter Selection", "publications", "low", "Filter publications by publication year", "Displays papers published in selected year"),
        ("Mobile Publications Filter Reset", "publications", "low", "Tap 'Reset' on publications filter", "Clears search and filters on publications screen"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_modules, start=166):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 6. Mobile Analytics, Favorites & Admin (APP-206 - APP-250) = 45
    mobile_analytics = [
        ("Mobile Analytics Screen Initial Load", "analytics", "critical", "Navigate to Analytics tab on mobile", "Displays statistical summary cards and charts"),
        ("Mobile Analytics Total Genes Metric Card", "analytics", "high", "Inspect Total Genes counter card on mobile", "Displays numerical count of genes in database"),
        ("Mobile Analytics Total Diseases Card", "analytics", "high", "Inspect Total Diseases metric card", "Displays total count of curated diseases"),
        ("Mobile Analytics Total Associations Card", "analytics", "high", "Inspect Total Associations metric card", "Displays total disease-gene pairs count"),
        ("Mobile Analytics Total Variants Card", "analytics", "high", "Inspect Total Variants metric card", "Displays total variant count"),
        ("Mobile Analytics Chromosome Chart on Mobile", "analytics", "high", "Inspect Chromosome Distribution chart on mobile", "Chart renders responsively within screen boundaries"),
        ("Mobile Analytics Pathogenicity Chart on Mobile", "analytics", "high", "Inspect Pathogenicity chart on mobile screen", "Donut chart renders with touch legend"),
        ("Mobile Analytics Chart Tap for Tooltip", "analytics", "medium", "Tap on chart slice with touch finger", "Tooltip appears showing exact count for touched category"),
        ("Mobile Analytics Pull to Refresh Stats", "analytics", "medium", "Pull down from top of analytics screen", "Refreshes statistics data from server"),
        ("Mobile AI Insights Graph Screen Load", "ai-insights", "high", "Open AI Insights network visualization on mobile", "Graph canvas renders with mobile touch controls"),
        ("Mobile AI Insights Pan Gesture on Canvas", "ai-insights", "medium", "Drag finger across graph canvas", "Canvas pans following finger movement"),
        ("Mobile AI Insights Pinch Gesture to Zoom", "ai-insights", "medium", "Pinch on network canvas", "Canvas zooms in and out responsively"),
        ("Mobile AI Insights Node Tap Inspection", "ai-insights", "high", "Tap gene node on mobile network graph", "Bottom sheet displays node details and connections"),
        ("Mobile Favorites Screen Initial Load", "favorites", "critical", "Navigate to Favorites screen from bottom nav", "Displays user's saved genes and diseases tabs"),
        ("Mobile Favorites Saved Genes Tab", "favorites", "high", "Tap 'Saved Genes' tab on mobile favorites", "Displays list of favorited gene cards"),
        ("Mobile Favorites Saved Diseases Tab", "favorites", "high", "Tap 'Saved Diseases' tab on mobile favorites", "Displays list of favorited disease cards"),
        ("Mobile Favorites Empty State Display", "favorites", "medium", "Open favorites when no items are favorited", "Displays friendly 'No favorites saved yet' message"),
        ("Mobile Favorites Tap Card Navigation", "favorites", "high", "Tap saved gene card in favorites list", "Navigates directly to that gene's detail screen"),
        ("Mobile Favorites Unfavorite Action", "favorites", "high", "Tap heart icon on saved item in favorites list", "Item removed from favorites with undo toast"),
        ("Mobile Admin Screen Access with Admin User", "admin", "critical", "Login as Admin and open Admin screen on mobile", "Displays admin system overview and management tabs"),
        ("Mobile Admin Screen Block for Researcher User", "admin", "critical", "Login as Researcher and open Admin screen", "Displays 'Admin access required' authorization block"),
        ("Mobile Admin Overview Metric Cards", "admin", "high", "Inspect admin overview counters on mobile", "Displays gene, disease, variant, pathway counts"),
        ("Mobile Admin Profile Update Form", "admin", "high", "Open Admin Profile settings on mobile", "Inputs: Admin username, Admin email"),
        ("Mobile Admin Profile Submit Update", "admin", "high", "Update email on mobile and tap 'Save Changes'", "Profile saved with confirmation snackbar"),
        ("Mobile Database Explorer View on Mobile", "database", "medium", "Navigate to Database Explorer on mobile", "Displays table schema selector and data preview"),
        ("Mobile Database Explorer Switch Table", "database", "medium", "Switch database table selector to 'Diseases'", "Preview updates with disease table rows"),
        ("Mobile Database Explorer CSV Export Trigger", "database", "low", "Tap 'Export CSV' button on mobile explorer", "File download initiated on device"),
        ("Mobile Settings Screen Display", "settings", "high", "Open Settings from mobile More menu", "Displays Account, Notifications, Theme, About options"),
        ("Mobile Settings App Version Display", "settings", "low", "Inspect App Version row in settings", "Displays 'Version 1.0.0 (Capacitor Android)'"),
        ("Mobile Settings Cache Clear Action", "settings", "low", "Tap 'Clear Local Cache' button in settings", "Local storage cache cleared with success message"),
        ("Mobile Settings Privacy Policy Link", "settings", "low", "Tap 'Privacy Policy' row in settings", "Opens privacy policy in Chrome Custom Tab"),
        ("Mobile Settings Terms of Service Link", "settings", "low", "Tap 'Terms of Service' in settings", "Opens terms of service in browser"),
        ("Mobile Notifications Permission Dialog", "device", "medium", "Trigger notifications toggle in settings", "Android system notification permission prompt shown"),
        ("Mobile Network Status Indicator Bar", "network", "medium", "Toggle network connection state", "Offline status indicator bar shows when disconnected"),
        ("Mobile SSL / TLS Certificate Validation", "security", "high", "Verify HTTPS connection security on mobile API requests", "App enforces valid SSL/TLS certificates"),
        ("Mobile Secure Storage of Auth Tokens", "security", "critical", "Inspect auth token storage mechanism on mobile", "Token stored in secure Capacitor Preferences/storage"),
        ("Mobile Deep Link Route Handling", "navigation", "medium", "Simulate deep link 'diseasegene://genes/BRCA1'", "App opens directly to BRCA1 detail screen"),
        ("Mobile Deep Link Disease Route", "navigation", "medium", "Simulate deep link 'diseasegene://diseases/DIS001'", "App opens directly to specified disease screen"),
        ("Mobile Invalid Deep Link 404 Fallback", "navigation", "low", "Simulate deep link to non-existent route", "App opens cleanly and falls back to home screen"),
        ("Mobile Android 13 Themed App Icon", "ui", "low", "Inspect launcher icon on Android 13 emulator", "Themed monochrome icon renders correctly"),
        ("Mobile Android App Permissions Audit", "security", "high", "Check declared permissions in AndroidManifest.xml", "Only INTERNET permission requested; no dangerous permissions"),
        ("Mobile App Signature Verification", "security", "medium", "Verify APK signature with apksigner tool", "APK properly signed with valid debug/release keystore"),
        ("Mobile Memory Leak Check After 20 Navigations", "performance", "medium", "Navigate back and forth between screens 20 times", "Heap memory stabilizes without leak accumulation"),
        ("Mobile Frame Rate / Jank Audit (60fps)", "performance", "medium", "Scroll list while profiling frame renders", "Maintains smooth 60fps scrolling without dropped frames"),
        ("Mobile Startup Time Benchmark (< 2.5s)", "performance", "high", "Measure cold startup time from adb launch", "App fully interactive within 2.5 seconds"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_analytics, start=206):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 7. Mobile Edge Cases, Network & Device Integration (APP-251 - APP-300) = 50
    mobile_edge = [
        ("Mobile Offline Mode Banner Appearance", "network", "critical", "Disable WiFi/cellular on emulator", "Top banner shows 'You are currently offline'"),
        ("Mobile Offline Mode Banner Dismissal", "network", "critical", "Re-enable internet on emulator", "Banner shows 'Back online' then dismisses"),
        ("Mobile Offline Cached Feed Viewing", "network", "high", "View previously loaded genes while offline", "Cached genes render from local storage without error"),
        ("Mobile Offline Mutating Action Block", "network", "high", "Attempt to favorite gene while offline", "Alert displays 'Action requires an internet connection'"),
        ("Mobile Slow 3G Network Latency Handling", "network", "medium", "Throttle emulator network to Slow 3G", "App displays loading spinner without premature timeout"),
        ("Mobile API 500 Server Error Alert", "error-handling", "high", "Simulate server 500 error on mobile API call", "Displays friendly error card 'Server temporarily unavailable'"),
        ("Mobile API 404 Not Found Handling", "error-handling", "medium", "Navigate to deleted gene ID on mobile", "Displays 'Item not found' with button to return to catalog"),
        ("Mobile Session Token Tampering Defense", "security", "high", "Corrupt stored JWT token in mobile storage", "App detects invalid token, purges it, and redirects to login"),
        ("Mobile Screen Lock During Active Request", "device", "medium", "Lock screen while search request is in-flight", "Request completes and state updates cleanly upon unlock"),
        ("Mobile Rapid Double Tap Prevention on Forms", "ui", "medium", "Rapidly double tap Sign In button", "Second tap ignored; only single API request submitted"),
        ("Mobile Device Rotation During Video/Chart View", "device", "medium", "Rotate screen to landscape while viewing charts", "Chart resizes to fill landscape width cleanly"),
        ("Mobile Keyboard Push-Up Layout Adjust", "ui", "medium", "Open keyboard on bottom form input", "Screen scrolls up automatically so input remains visible above keyboard"),
        ("Mobile Android Back Gesture During Search", "navigation", "medium", "Perform back gesture while search query active", "Clears search input first before exiting search screen"),
        ("Mobile Text Selection in Descriptions", "ui", "low", "Long press on scientific description text", "Selection handles appear allowing text copy"),
        ("Mobile Webview Hardware Acceleration", "performance", "medium", "Verify Android hardware acceleration enabled", "Hardware acceleration enabled for smooth rendering"),
        ("Mobile Clear App Data from Android Settings", "device", "medium", "Clear storage & cache from Android Settings", "App resets cleanly to first-launch state on next start"),
        ("Mobile App Update Simulation", "lifecycle", "low", "Install updated APK over existing version", "User session and preferences preserved across app update"),
        ("Mobile Android 14 Compatibility Check", "device", "medium", "Execute tests on Android 14 (API 34) emulator", "App runs without deprecation warnings or crashes"),
        ("Mobile Android 12 Compatibility Check", "device", "medium", "Execute tests on Android 12 (API 31) emulator", "App runs backwards-compatible without issues"),
        ("Mobile Tablet 10-inch Emulator Layout", "ui", "medium", "Launch app on 10-inch Android tablet emulator", "Layout adapts to split-pane master-detail view"),
        ("Mobile Foldable Device Fold / Unfold", "device", "low", "Simulate screen unfold on foldable emulator", "Viewport adapts smoothly to expanded aspect ratio"),
        ("Mobile System Locale Change to Spanish", "localization", "low", "Change Android system language to Spanish", "App defaults to English gracefully or localized strings"),
        ("Mobile Right-to-Left (RTL) Layout Mode", "localization", "low", "Enable 'Force RTL layout' in Android developer options", "Layout elements mirror correctly without visual breakage"),
        ("Mobile Battery Saver Mode Interaction", "device", "low", "Enable Android Battery Saver mode", "App reduces background sync and animations gracefully"),
        ("Mobile Low Storage Space Warning", "device", "low", "Simulate device storage under 50MB", "App handles local cache write gracefully without crash"),
        ("Mobile Clipboard Copy Gene Symbol Toast", "ui", "low", "Tap copy icon next to gene symbol", "Android toast confirms 'Gene symbol copied to clipboard'"),
        ("Mobile Paste from Clipboard into Search", "ui", "low", "Long press in search input and select Paste", "Pasted text populates search input and triggers search"),
        ("Mobile Capacitor Bridge Plugin Call Timeout", "performance", "medium", "Simulate delayed response from native bridge", "App handles timeout gracefully without UI freeze"),
        ("Mobile WebView Console Log Suppression", "security", "medium", "Inspect Android logcat output in production build", "Sensitive tokens and data not printed to system logcat"),
        ("Mobile ProGuard / R8 Obfuscation Check", "security", "high", "Inspect release APK build with dex analysis", "Code properly obfuscated with shrunk unused resources"),
        ("Mobile APK File Size Optimization (< 15MB)", "performance", "medium", "Check size of output app-debug.apk", "APK size optimized below acceptable threshold"),
        ("Mobile Launch Time Warm Start Benchmark", "performance", "medium", "Measure warm start time from background", "Warm start finishes under 500 milliseconds"),
        ("Mobile Image Asset Density Qualification", "ui", "low", "Check icons across mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi", "Crisp icon assets rendered for each device density"),
        ("Mobile Push Notification Payload Receive", "network", "low", "Simulate push notification reception", "Notification received without crashing app"),
        ("Mobile Push Notification Tap Deep Link", "navigation", "medium", "Tap incoming notification banner", "App opens directly to target notification item"),
        ("Mobile Backstack Depth Limit Handling", "navigation", "low", "Navigate through 15 nested detail screens", "Hardware back button unwinds navigation stack accurately"),
        ("Mobile Screen Time-Out Keep Screen On in Graph", "device", "low", "Inspect keepScreenOn flag on AI Insights canvas", "Screen dimming handled appropriately"),
        ("Mobile Audio Focus Handling", "device", "low", "Play background audio while in app", "App does not interrupt external media playback"),
        ("Mobile Touch Responsiveness (< 100ms)", "performance", "medium", "Measure input latency on button tap", "Touch feedback visible within 100ms"),
        ("Mobile Android StrictMode Policy Violation Check", "performance", "medium", "Run app with Android StrictMode enabled", "No disk reads or network calls on main UI thread"),
        ("Mobile Android 13 Granular Media Permissions", "permissions", "low", "Verify app does not request obsolete READ_EXTERNAL_STORAGE", "Compliant with Android 13 permissions model"),
        ("Mobile Backpress Double-Tap to Exit App", "navigation", "medium", "Press back twice on home screen", "Shows 'Press back again to exit' and closes app on second tap"),
        ("Mobile Scroll Speed Acceleration Curve", "gestures", "low", "Verify natural Android physics scroll curve", "Scrolling adheres to platform standard friction curve"),
        ("Mobile Search Clear on Tab Navigation Away", "ui", "low", "Switch tabs while search query typed", "Search state preserved or cleanly reset on tab return"),
        ("Mobile Dark Mode Contrast in Direct Sunlight", "ui", "low", "Simulate high ambient brightness", "Text remains readable with sufficient contrast"),
        ("Mobile Android App Shortcut Long-Press", "navigation", "low", "Long press app launcher icon on Android home", "Displays app shortcuts: 'Search', 'Saved Genes'"),
        ("Mobile Tap Target Spacing Verification", "ui", "low", "Verify spacing between adjacent clickable chips", "Minimum 8dp separation prevents accidental mistaps"),
        ("Mobile Android Safe Browsing Verification", "security", "medium", "Verify WebView Safe Browsing configuration", "WebView safe browsing client enabled"),
        ("Mobile Certificate Pinning Evaluation", "security", "medium", "Inspect network security config XML", "Cleartext traffic disabled (cleartext: false in Capacitor config)"),
        ("Mobile Final E2E Critical User Journey", "e2e", "critical", "Login -> Search Gene -> View Detail -> Favorite -> Verify in Favorites", "Full end-to-end mobile research flow succeeds without error"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(mobile_edge, start=251):
        cases.append({"id": f"APP-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    return cases


def generate_load_cases():
    cases = []
    
    # 1. Smoke Profile Scenarios (LOAD-001 - LOAD-040) = 40
    smoke_defs = [
        ("Root Welcome Endpoint Smoke Check", "smoke", "critical", "Send GET / with 1 VU for 5s", "HTTP 200 returned with message and docs_url in < 100ms"),
        ("API Health Endpoint Smoke Check", "smoke", "critical", "Send GET /health with 1 VU for 5s", "HTTP 200 returned with healthy status in < 100ms"),
        ("API Stats Overview Endpoint Smoke", "smoke", "critical", "Send GET /api/v1/stats with 2 VUs for 10s", "HTTP 200 with counts and distribution data in < 300ms"),
        ("Genes Catalog Default Limit Smoke", "smoke", "high", "Send GET /api/v1/genes with 2 VUs", "HTTP 200 with 100 gene records in < 250ms"),
        ("Gene Detail Lookup by ID Smoke", "smoke", "high", "Send GET /api/v1/genes/BRCA1 with 2 VUs", "HTTP 200 with complete gene metadata in < 150ms"),
        ("Diseases Catalog Default Limit Smoke", "smoke", "high", "Send GET /api/v1/diseases with 2 VUs", "HTTP 200 with disease list in < 250ms"),
        ("Disease Detail Lookup by ID Smoke", "smoke", "high", "Send GET /api/v1/diseases/DIS001 with 2 VUs", "HTTP 200 with disease metadata in < 150ms"),
        ("Variants Catalog Endpoint Smoke", "smoke", "high", "Send GET /api/v1/variants with 2 VUs", "HTTP 200 with variants list in < 250ms"),
        ("Pathways Catalog Endpoint Smoke", "smoke", "high", "Send GET /api/v1/pathways with 2 VUs", "HTTP 200 with pathways list in < 250ms"),
        ("Associations Catalog Endpoint Smoke", "smoke", "high", "Send GET /api/v1/associations with 2 VUs", "HTTP 200 with associations list in < 250ms"),
        ("Drugs Catalog Endpoint Smoke", "smoke", "medium", "Send GET /api/v1/drugs with 2 VUs", "HTTP 200 with drug records in < 250ms"),
        ("Publications Catalog Endpoint Smoke", "smoke", "medium", "Send GET /api/v1/publications with 2 VUs", "HTTP 200 with publication records in < 250ms"),
        ("Global Search Empty Query Smoke", "smoke", "medium", "Send GET /api/v1/search?q= with 2 VUs", "HTTP 200 with empty results list in < 150ms"),
        ("Global Search Keyword 'TP53' Smoke", "smoke", "high", "Send GET /api/v1/search?q=TP53 with 2 VUs", "HTTP 200 with search results in < 350ms"),
        ("Auth Login Endpoint Smoke", "smoke", "critical", "Send POST /api/v1/auth/login with valid form data", "HTTP 200 with Bearer JWT access token in < 200ms"),
        ("Auth Get Me Endpoint Smoke", "smoke", "high", "Send GET /api/v1/auth/me with Bearer token", "HTTP 200 with current user profile in < 150ms"),
        ("Admin Overview Endpoint Smoke", "smoke", "high", "Send GET /api/v1/admin/overview with Admin token", "HTTP 200 with admin counts in < 200ms"),
        ("OpenAPI Schema Specification Smoke", "smoke", "low", "Send GET /api/v1/openapi.json", "HTTP 200 returning valid OpenAPI 3.0 JSON schema"),
        ("API Docs Swagger UI Smoke", "smoke", "low", "Send GET /docs", "HTTP 200 returning Swagger interactive documentation"),
        ("API Redoc UI Smoke", "smoke", "low", "Send GET /redoc", "HTTP 200 returning Redoc interface"),
        ("Gene Filter by Chromosome 1 Smoke", "smoke", "medium", "Send GET /api/v1/genes?chromosome=1", "HTTP 200 with Chr 1 genes in < 250ms"),
        ("Gene Filter by Chromosome X Smoke", "smoke", "medium", "Send GET /api/v1/genes?chromosome=X", "HTTP 200 with Chr X genes in < 250ms"),
        ("Gene Pagination Skip 50 Smoke", "smoke", "medium", "Send GET /api/v1/genes?skip=50&limit=50", "HTTP 200 with offset items in < 200ms"),
        ("Disease Search by Category Smoke", "smoke", "medium", "Send GET /api/v1/diseases?category=Cancer", "HTTP 200 with oncology diseases in < 250ms"),
        ("Variant Filter by ClinSig Pathogenic Smoke", "smoke", "medium", "Send GET /api/v1/variants?clinical_significance=Pathogenic", "HTTP 200 in < 250ms"),
        ("Pathway Detail by ID Smoke", "smoke", "medium", "Send GET /api/v1/pathways/PW001", "HTTP 200 with pathway genes in < 200ms"),
        ("Association Filter by Evidence Level A Smoke", "smoke", "medium", "Send GET /api/v1/associations?evidence_level=A", "HTTP 200 in < 250ms"),
        ("Drug Search by Action Inhibitor Smoke", "smoke", "low", "Send GET /api/v1/drugs?action=Inhibitor", "HTTP 200 in < 200ms"),
        ("Publication Search by Year 2023 Smoke", "smoke", "low", "Send GET /api/v1/publications?year=2023", "HTTP 200 in < 200ms"),
        ("Search Filter by Type 'gene' Smoke", "smoke", "medium", "Send GET /api/v1/search?q=BRCA&type=gene", "HTTP 200 with gene-only results in < 300ms"),
        ("Search Filter by Type 'disease' Smoke", "smoke", "medium", "Send GET /api/v1/search?q=Cancer&type=disease", "HTTP 200 with disease results in < 300ms"),
        ("Forgot Password Request Endpoint Smoke", "smoke", "medium", "Send POST /api/v1/auth/forgot-password", "HTTP 200 returning success confirmation"),
        ("Favorite Gene Add Smoke Check", "smoke", "high", "Send POST /api/v1/genes/BRCA1/favorite with auth", "HTTP 201 or 200 indicating favorited"),
        ("Favorite Gene Delete Smoke Check", "smoke", "high", "Send DELETE /api/v1/genes/BRCA1/favorite with auth", "HTTP 200 indicating unfavorited"),
        ("Admin Update Profile Smoke Check", "smoke", "medium", "Send PUT /api/v1/admin/profile with Admin auth", "HTTP 200 returning updated profile"),
        ("Non-Existent Endpoint 404 Smoke Check", "smoke", "low", "Send GET /api/v1/nonexistent-route", "HTTP 404 handled cleanly in < 50ms"),
        ("Invalid Method 405 Smoke Check", "smoke", "low", "Send POST to GET-only /api/v1/stats", "HTTP 405 Method Not Allowed in < 50ms"),
        ("Unauthenticated Access 401 Smoke Check", "smoke", "medium", "Send GET /api/v1/auth/me without token", "HTTP 401 Unauthorized in < 50ms"),
        ("Forbidden Access 403 Smoke Check", "smoke", "medium", "Send GET /api/v1/admin/overview with researcher token", "HTTP 403 Forbidden in < 50ms"),
        ("Smoke Profile Overall Threshold Verification", "smoke", "critical", "Verify smoke profile latency across all 40 endpoints", "p95 < 300ms, error rate 0.00%"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(smoke_defs, start=1):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 2. Normal Load Profile Scenarios (LOAD-041 - LOAD-100) = 60
    load_defs = []
    entities = ["genes", "diseases", "variants", "pathways", "associations", "drugs", "publications", "search"]
    for idx in range(41, 101):
        ent = entities[(idx - 41) % len(entities)]
        step = (idx - 41) // len(entities) + 1
        name = f"Normal Load on {ent.capitalize()} Step {step}"
        desc = f"Simulate concurrent user traffic on /{ent} with 30-50 VUs sustained for 3 minutes"
        exp = "p95 < 450ms, p99 < 800ms, error rate < 0.5%"
        load_defs.append((name, "load", "high", desc, exp))
    for i, (name, cat, prio, desc, exp) in enumerate(load_defs, start=41):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 3. Stress Profile Scenarios (LOAD-101 - LOAD-160) = 60
    stress_defs = []
    for idx in range(101, 161):
        vu_level = 100 + ((idx - 101) % 5) * 80  # 100, 180, 260, 340, 420 VUs
        area = entities[(idx - 101) % len(entities)]
        name = f"Stress Testing {area.capitalize()} at {vu_level} VUs"
        desc = f"Ramp up load to {vu_level} concurrent virtual users targeting {area} to find performance saturation point"
        exp = f"System sustains throughput without worker crash; error rate < 2.0% under {vu_level} VUs"
        stress_defs.append((name, "stress", "high", desc, exp))
    for i, (name, cat, prio, desc, exp) in enumerate(stress_defs, start=101):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 4. Spike Profile Scenarios (LOAD-161 - LOAD-200) = 40
    spike_defs = []
    for idx in range(161, 201):
        target = ["/api/v1/search?q=BRCA1", "/api/v1/stats", "/api/v1/genes", "/api/v1/diseases", "/api/v1/associations"][(idx - 161) % 5]
        name = f"Spike Traffic Burst #{idx - 160} on {target.split('?')[0]}"
        desc = f"Surge from 10 to 500 VUs in 15 seconds targeting {target}, hold for 30s, drop to 10 VUs"
        exp = "Server absorbs spike without service crash; latency recovers to baseline within 15s after spike"
        spike_defs.append((name, "spike", "high", desc, exp))
    for i, (name, cat, prio, desc, exp) in enumerate(spike_defs, start=161):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 5. Soak / Endurance Profile (LOAD-201 - LOAD-240) = 40
    soak_defs = []
    for idx in range(201, 241):
        hour = ((idx - 201) // 10) + 1
        substep = (idx - 201) % 10 + 1
        name = f"Soak Endurance Hour {hour} Sub-scenario {substep}"
        desc = f"Execute continuous steady-state load with 40 VUs monitoring memory and connection pools"
        exp = "Zero memory leak, stable latency drift (< 10% variance), connection pool remains healthy"
        soak_defs.append((name, "soak", "medium", desc, exp))
    for i, (name, cat, prio, desc, exp) in enumerate(soak_defs, start=201):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 6. API Performance & DB-Heavy Operations (LOAD-241 - LOAD-275) = 35
    api_defs = [
        ("Stats Endpoint Aggregation Query Under Load", "api", "critical", "Execute /api/v1/stats with 50 concurrent requests", "p95 < 400ms across SQL group_by aggregations"),
        ("Deep Pagination Offset skip=1000 limit=100", "api", "high", "Request /api/v1/genes?skip=1000&limit=100 under concurrency", "Query executes efficiently using indexed keys"),
        ("Deep Pagination Offset skip=5000 limit=100", "api", "high", "Request /api/v1/diseases?skip=5000&limit=100", "Response returned within 500ms"),
        ("Chromosome Distribution Query Concurrency", "api", "high", "50 concurrent clients requesting chromosome distribution", "Database handles group-by without thread exhaustion"),
        ("Evidence Level Aggregation Query Concurrency", "api", "high", "50 concurrent clients requesting pathogenicity distribution", "Database responds in < 350ms"),
        ("Full-Text Search Fallback Under High Load", "api", "critical", "100 concurrent search queries using SQL ILIKE fallback", "Database query optimizer handles LIKE wildcard without table locks"),
        ("Multi-Column Search Filtering Under Load", "api", "high", "Concurrent search with multi-field matching", "p95 < 600ms during multi-field ILIKE queries"),
        ("Filtered Associations Query with High Offsets", "api", "medium", "Filter associations by evidence level with pagination", "Response returned in < 450ms"),
        ("Variant Filtering by Mutation and ClinSig", "api", "medium", "Query variants with compound filters under load", "Index utilized effectively with p95 < 400ms"),
        ("Pathway Genes Subquery Under Load", "api", "medium", "Concurrent requests for pathway detail with associated genes", "p95 < 350ms"),
        ("Drug Targets Query with Mechanism Filters", "api", "low", "Concurrent queries on /api/v1/drugs with filters", "p95 < 300ms"),
        ("Publication Search by Year Range Under Load", "api", "low", "Concurrent queries on /api/v1/publications", "p95 < 300ms"),
        ("Simultaneous Read and Write Transactions", "api", "critical", "50 concurrent reads alongside 10 concurrent favorites writes", "Zero deadlocks; ACID transactions commit cleanly"),
        ("Concurrent Favorite Gene Insertions", "api", "high", "50 users simultaneously favoriting different genes", "Row locks minimized; all writes complete successfully"),
        ("Concurrent Favorite Gene Deletions", "api", "high", "50 users simultaneously unfavoriting genes", "Deletes complete without orphan records or deadlocks"),
        ("Admin Overview Dashboard Load", "api", "high", "25 concurrent requests to /api/v1/admin/overview", "All 5 table counts execute in < 300ms total"),
        ("Admin Profile Update Concurrency", "api", "medium", "Concurrent profile update requests", "Row locking isolates updates without data corruption"),
        ("Large Result Payload Serialization (limit=500)", "api", "medium", "Request /api/v1/genes?limit=500 with 20 VUs", "FastAPI Pydantic serialization executes in < 400ms"),
        ("Large Result Payload Serialization (limit=1000)", "api", "medium", "Request /api/v1/variants?limit=1000 with 10 VUs", "Payload streamed without memory exhaustion"),
        ("Database Connection Pool Max Saturation", "api", "critical", "Surpass pool size with 150 concurrent DB queries", "Requests queue cleanly without dropping connections"),
        ("Database Connection Recovery After Release", "api", "high", "Check connection pool latency immediately after burst", "Connections returned to pool instantly"),
        ("Database Vacuum and Query Performance", "api", "low", "Measure query latency after bulk inserts", "Indices remain optimal without table fragmentation"),
        ("Complex Search Query with Special Characters", "api", "medium", "Fuzz search endpoint with symbols under load", "Zero 500 crashes; handles input cleanly in < 300ms"),
        ("HTTP Compression (Gzip) Throughput", "api", "medium", "Verify Gzip compression of large JSON payloads under load", "Bandwidth reduced by > 70% with negligible CPU overhead"),
        ("Keep-Alive HTTP Connection Reuse Benchmark", "api", "high", "Benchmark HTTP keep-alive vs new TCP connection per request", "Keep-alive yields > 3x higher throughput"),
        ("Uvicorn Worker Process CPU Utilization", "api", "medium", "Monitor worker CPU under 100 sustained VUs", "CPU utilization distributed evenly across workers"),
        ("SQLite / Postgres File I/O Lock Latency", "api", "high", "Measure disk I/O wait times under sustained queries", "I/O wait remains under 15ms"),
        ("FastAPI Dependency Injection Overhead", "api", "low", "Benchmark endpoint with multi-level deps vs direct handler", "Dependency overhead < 2ms per request"),
        ("CORS Preflight (OPTIONS) Request Performance", "api", "medium", "500 concurrent OPTIONS preflight requests", "Preflight responses cached and served in < 20ms"),
        ("ETL Ingestion Script Database Lock Impact", "api", "medium", "Simulate ETL batch insert while API queries in-flight", "API queries continue executing without transaction timeout"),
        ("Search Autocomplete Query Rapid Typing Latency", "api", "high", "Simulate 5 keystrokes per second per VU on search", "Debounced response times remain under 200ms"),
        ("Disease OMIM Lookup Latency Under Concurrency", "api", "low", "50 concurrent queries for disease records", "p95 < 250ms"),
        ("Gene Protein Annotation Fetch Throughput", "api", "low", "Concurrent queries for gene protein annotations", "p95 < 250ms"),
        ("Publication Abstract Payload Serialization", "api", "low", "Query 100 publications with full text abstracts", "Serialization finishes in < 350ms"),
        ("Comprehensive API SLA Validation Benchmark", "api", "critical", "Run 10-minute mixed API workload across all endpoints", "Global p95 < 400ms, error rate < 0.1%"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(api_defs, start=241):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 7. Authentication & Security Load (LOAD-276 - LOAD-300) = 25
    auth_load_defs = [
        ("Concurrent User Registration Rate", "authentication", "critical", "50 concurrent registration requests with unique credentials", "User accounts created without unique constraint race conditions"),
        ("Password Hashing (Bcrypt) CPU Load", "authentication", "high", "Simulate 30 concurrent password hashing operations", "Bcrypt work factor balanced; CPU handles hash in < 300ms"),
        ("OAuth2 Password Flow Login Concurrency", "authentication", "critical", "100 concurrent logins with valid user credentials", "JWT tokens generated and returned with p95 < 350ms"),
        ("Bearer Token Verification Throughput", "authentication", "critical", "500 requests per second to /api/v1/auth/me with Bearer JWT", "JWT cryptographic signature verification executes in < 5ms"),
        ("Concurrent Failed Login Attempts", "authentication", "high", "100 concurrent logins with incorrect password", "Authentication correctly rejects with 401 without server crash"),
        ("Brute Force Attack Simulation on /auth/login", "authentication", "high", "Send 1,000 rapid login requests for single user", "System resists brute force; response latency remains steady"),
        ("Forgot Password OTP Generation Under Load", "authentication", "medium", "50 concurrent forgot-password OTP requests", "OTPs generated and stored without collision or failure"),
        ("Reset Password with OTP Verification Concurrency", "authentication", "medium", "30 concurrent reset-password requests with valid OTPs", "Passwords updated cleanly with p95 < 400ms"),
        ("Expired JWT Token Handling Under High Load", "authentication", "medium", "200 concurrent requests sending expired JWTs", "All rejected with 401 in < 20ms without database hits"),
        ("Malformed JWT Token Rejection Performance", "authentication", "low", "200 concurrent requests sending garbled JWT tokens", "Cryptographic parse error caught immediately in < 10ms"),
        ("Concurrent Registration with Duplicate Data", "authentication", "high", "50 concurrent requests trying to register existing username", "All return 400 'already registered' without unhandled errors"),
        ("Concurrent User Logout / Session Clear", "authentication", "low", "50 concurrent logout / token discard actions", "Session states invalidated without error"),
        ("Clear Stuck User Cleanup Endpoint Under Load", "authentication", "low", "Concurrent requests to clear-stuck-user endpoint", "Database cleans target records without deadlock"),
        ("First User Registration Admin Promotion Race Condition", "authentication", "high", "Concurrent registrations on empty database", "Exactly one user receives Admin role; others receive Researcher"),
        ("JWT Secret Key Verification Under Sustained Load", "authentication", "medium", "Verify JWT signature verification does not leak memory", "Memory remains flat over 100,000 token checks"),
        ("Access Token Expiration Delta Computation", "authentication", "low", "Benchmark token expiry generation overhead", "Overhead < 1ms per token"),
        ("Email Service Mock Queue Under Load", "authentication", "medium", "50 concurrent OTP email trigger requests", "Email dispatcher queues notifications without blocking API"),
        ("Admin Role Validation Middleware Latency", "authentication", "medium", "100 concurrent requests checking role=='Admin'", "Role check dependency adds < 5ms to request cycle"),
        ("Researcher Role Restriction Middleware Latency", "authentication", "medium", "100 concurrent forbidden requests to admin route", "Rejections returned in < 25ms"),
        ("User Query /auth/me Database Index Efficiency", "authentication", "high", "Query /auth/me concurrently by username index", "Indexed lookup finishes in < 15ms"),
        ("Simultaneous Login and Profile Update", "authentication", "medium", "User logs in while updating profile from another device", "Both transactions complete with consistent state"),
        ("Password Complexity Validation Throughput", "authentication", "low", "Run 1,000 password complexity checks per second", "Regex validation executes in < 0.5ms per password"),
        ("Token Payload Size Impact on Network", "authentication", "low", "Measure transmission overhead of JWT token headers", "Compact JWT minimizes HTTP header overhead (< 500 bytes)"),
        ("High Volume Session Re-authentication", "authentication", "medium", "50 users re-authenticating after session expiration", "Tokens refreshed smoothly with p95 < 300ms"),
        ("End-to-End High Concurrency User Journey", "authentication", "critical", "Register -> Login -> Fetch Profile -> Search -> Favorite -> Logout under load", "Full authenticated researcher journey completes with 99.9% success rate"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(auth_load_defs, start=276):
        cases.append({"id": f"LOAD-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    return cases


def generate_security_cases():
    cases = []
    
    # 1. Security Headers & Transport Security (SEC-001 - SEC-045) = 45
    header_defs = [
        ("Strict-Transport-Security (HSTS) Header Presence", "headers", "critical", "Inspect HSTS header on HTTPS responses", "max-age >= 31536000 and includeSubDomains present"),
        ("X-Content-Type-Options Header Verification", "headers", "high", "Inspect X-Content-Type-Options header on API responses", "Header set to 'nosniff' preventing MIME sniffing"),
        ("X-Frame-Options Header Check", "headers", "high", "Verify X-Frame-Options on web pages", "Header set to 'DENY' or 'SAMEORIGIN' preventing clickjacking"),
        ("Content-Security-Policy (CSP) Directives", "headers", "critical", "Verify CSP header on web responses", "Valid CSP restricting default-src, script-src, object-src"),
        ("Referrer-Policy Header Check", "headers", "medium", "Verify Referrer-Policy header", "Set to 'strict-origin-when-cross-origin' or 'no-referrer'"),
        ("Permissions-Policy Header Check", "headers", "medium", "Verify Permissions-Policy header", "Restricts camera, microphone, geolocation APIs"),
        ("Server Banner Information Disclosure", "headers", "high", "Inspect Server header on responses", "Server banner does not expose exact uvicorn/fastapi version"),
        ("X-Powered-By Header Suppression", "headers", "medium", "Check for X-Powered-By header", "X-Powered-By header omitted from responses"),
        ("Cache-Control on Sensitive Endpoints (/auth/me)", "headers", "high", "Check Cache-Control on /auth/me", "Set to 'no-store, no-cache, must-revalidate'"),
        ("Cache-Control on Login Endpoint (/auth/login)", "headers", "high", "Check Cache-Control on /auth/login response", "Contains 'no-store' preventing credential caching"),
        ("Cache-Control on Admin Overview (/admin/overview)", "headers", "high", "Check Cache-Control on /admin/overview", "Contains 'no-store' preventing data caching"),
        ("Access-Control-Allow-Origin Configuration", "headers", "critical", "Check CORS headers with unauthorized origin", "Unauthorized origin rejected; wildcards not paired with credentials"),
        ("Access-Control-Allow-Credentials Security", "headers", "high", "Verify allow_credentials behavior with wildcard origin", "Wildcard '*' disallowed when allow_credentials is true"),
        ("Access-Control-Allow-Methods Restrictions", "headers", "medium", "Inspect allowed HTTP methods in CORS preflight", "Only necessary methods (GET, POST, PUT, DELETE, OPTIONS) allowed"),
        ("Access-Control-Allow-Headers Restrictions", "headers", "medium", "Inspect allowed headers in CORS preflight", "Only Authorization, Content-Type, and needed headers allowed"),
        ("Access-Control-Max-Age Header Check", "headers", "low", "Inspect CORS preflight max-age cache duration", "Max-age configured to reasonable duration (e.g., 600s)"),
        ("TLS 1.3 Protocol Support", "transport", "high", "Check TLS version negotiation", "TLS 1.3 accepted for encrypted transport"),
        ("TLS 1.2 Protocol Support with Strong Ciphers", "transport", "high", "Verify cipher suites on TLS 1.2", "Only secure cipher suites with forward secrecy allowed"),
        ("Insecure SSL v2/v3 and TLS 1.0/1.1 Rejection", "transport", "critical", "Attempt connection using deprecated TLS versions", "Connection rejected by server"),
        ("HTTPS Redirection from Plain HTTP", "transport", "high", "Send plain HTTP request to web portal", "Automatically redirected with 301/308 to HTTPS"),
        ("Cookie Secure Flag Verification", "headers", "high", "Inspect Set-Cookie headers for session cookies", "'Secure' flag set on all sensitive cookies"),
        ("Cookie HttpOnly Flag Verification", "headers", "high", "Inspect Set-Cookie headers for authentication cookies", "'HttpOnly' flag set preventing JavaScript access"),
        ("Cookie SameSite Flag Verification", "headers", "high", "Inspect Set-Cookie SameSite attribute", "SameSite set to 'Lax' or 'Strict' preventing CSRF"),
        ("Cookie Domain Scope Restriction", "headers", "medium", "Check Domain attribute on cookies", "Cookies restricted to exact application host"),
        ("Cookie Path Scope Restriction", "headers", "medium", "Check Path attribute on cookies", "Cookies scoped appropriately to application root"),
        ("Cleartext Traffic Disallowed in Android Manifest", "headers", "critical", "Inspect android:usesCleartextTraffic in AndroidManifest", "Cleartext traffic disallowed (cleartext: false)"),
        ("Cross-Origin-Opener-Policy (COOP) Check", "headers", "low", "Check COOP header", "Set to 'same-origin' or 'same-origin-allow-popups'"),
        ("Cross-Origin-Embedder-Policy (COEP) Check", "headers", "low", "Check COEP header", "Properly configured for resource isolation"),
        ("Cross-Origin-Resource-Policy (CORP) Check", "headers", "low", "Check CORP header", "Set to 'same-origin' or 'same-site'"),
        ("X-XSS-Protection Header Legacy Defense", "headers", "low", "Check legacy X-XSS-Protection header", "Set to '1; mode=block' or omitted in favor of CSP"),
        ("X-Download-Options for IE8 / Legacy Browsers", "headers", "low", "Check X-Download-Options header", "Set to 'noopen'"),
        ("X-DNS-Prefetch-Control Header Check", "headers", "low", "Check X-DNS-Prefetch-Control header", "Set to 'off' on sensitive pages"),
        ("Expect-CT Certificate Transparency Header", "headers", "low", "Inspect Expect-CT header if present", "Enforces certificate transparency"),
        ("ETag Header Information Leakage", "headers", "low", "Inspect ETag generation algorithm", "ETag does not reveal inode or sensitive server metadata"),
        ("Content-Type Character Encoding Specification", "headers", "medium", "Inspect Content-Type header on responses", "Specifies charset=utf-8 explicitly"),
        ("Security Headers on Error Responses (404/500)", "headers", "medium", "Inspect headers on 404 and 500 error responses", "Security headers maintained even during error responses"),
        ("Security Headers on Static Assets", "headers", "low", "Inspect headers on static JS/CSS files", "Cache-Control and X-Content-Type-Options present"),
        ("Security Headers on Redirect Responses (301/302)", "headers", "low", "Inspect headers on redirect responses", "Security headers preserved on redirects"),
        ("No-Sniff on Uploaded File Responses", "headers", "high", "Inspect responses from /backend/uploads", "X-Content-Type-Options nosniff enforced"),
        ("Content-Disposition Header on File Downloads", "headers", "high", "Inspect Content-Disposition on CSV exports", "Set to 'attachment; filename=...' preventing in-browser execution"),
        ("Subresource Integrity (SRI) on CDN Scripts", "headers", "medium", "Inspect script tags in frontend HTML", "External scripts include integrity hash and crossorigin attribute"),
        ("Robots.txt Sensitive Path Disallow", "headers", "low", "Inspect /robots.txt configuration", "Restricts indexing of /admin and /api endpoints"),
        ("Security.txt RFC 9116 Policy File", "headers", "low", "Inspect /.well-known/security.txt", "Provides security contact and disclosure policy"),
        ("CORS Preflight Caching Verification", "headers", "low", "Verify Access-Control-Max-Age avoids excessive preflights", "Configured appropriately"),
        ("Comprehensive HTTP Security Header Score", "headers", "high", "Audit overall security headers against Mozilla Observatory", "Achieves A/B grade on security header checklist"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(header_defs, start=1):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 2. Dependency Vulnerabilities & Supply Chain (SEC-046 - SEC-085) = 40
    dep_defs = [
        ("pip-audit Scan on FastAPI Framework", "dependencies", "critical", "Audit fastapi==0.104.1 for known CVE advisories", "No critical or high severity CVEs reported"),
        ("pip-audit Scan on Uvicorn ASGI Server", "dependencies", "critical", "Audit uvicorn==0.24.0.post1 for known vulnerabilities", "No known RCE or HTTP smuggling CVEs"),
        ("pip-audit Scan on SQLAlchemy ORM", "dependencies", "high", "Audit SQLAlchemy==2.0.23 for vulnerabilities", "No SQL injection or memory corruption CVEs"),
        ("pip-audit Scan on Pydantic Data Validator", "dependencies", "high", "Audit pydantic==2.5.2 for security advisories", "No denial-of-service or ReDoS vulnerabilities"),
        ("pip-audit Scan on python-jose / PyJWT", "dependencies", "critical", "Audit python-jose==3.5.0 and PyJWT==2.8.0", "No algorithm confusion or signature bypass CVEs"),
        ("pip-audit Scan on Passlib & Bcrypt", "dependencies", "critical", "Audit passlib==1.7.4 and bcrypt==4.0.1", "Password hashing libraries free from critical flaws"),
        ("pip-audit Scan on Cryptography Library", "dependencies", "critical", "Audit cryptography==47.0.0 for OpenSSL/crypto flaws", "Up-to-date cryptography package without known CVEs"),
        ("pip-audit Scan on Requests & HTTPX Libraries", "dependencies", "high", "Audit requests==2.32.5 and httpx==0.25.2", "No SSRF or header injection vulnerabilities"),
        ("pip-audit Scan on Pandas & NumPy", "dependencies", "medium", "Audit pandas==2.2.3 and numpy==1.26.4", "No arbitrary code execution in data parsing"),
        ("pip-audit Scan on Starlette Core", "dependencies", "high", "Audit starlette==0.27.0 for multipart/header flaws", "No multipart form parsing vulnerabilities"),
        ("pip-audit Scan on Elasticsearch Client", "dependencies", "medium", "Audit elasticsearch==8.11.0 client", "Client library secure against deserialization flaws"),
        ("pip-audit Full Requirements Scan", "dependencies", "critical", "Execute pip-audit across all packages in backend/requirements.txt", "Zero unpatched high or critical vulnerabilities"),
        ("npm audit Scan on Next.js Framework", "dependencies", "critical", "Audit next==14.2.15 for known CVE advisories", "No server-side request forgery or RSC vulnerabilities"),
        ("npm audit Scan on React & React-DOM", "dependencies", "critical", "Audit react==18.2.0 and react-dom==18.2.0", "Core React packages free from known XSS flaws"),
        ("npm audit Scan on Axios HTTP Client", "dependencies", "high", "Audit axios==1.6.2 for SSRF / prototype pollution", "No critical prototype pollution or SSRF CVEs"),
        ("npm audit Scan on Capacitor Android Core", "dependencies", "critical", "Audit @capacitor/core and @capacitor/android 8.4.0", "Capacitor runtime secure against bridge bypass flaws"),
        ("npm audit Scan on Plotly.js Visualization", "dependencies", "medium", "Audit plotly.js-dist-min==2.27.1", "No DOM-based XSS vulnerabilities in chart rendering"),
        ("npm audit Scan on D3.js Data Library", "dependencies", "medium", "Audit d3==7.8.5 for security advisories", "D3 packages free from known security vulnerabilities"),
        ("npm audit Full Package.json Scan", "dependencies", "critical", "Run npm audit in frontend directory", "Zero high or critical vulnerability findings"),
        ("Trivy Vulnerability Scan on Backend Filesystem", "dependencies", "critical", "Scan backend directory with Trivy vulnerability scanner", "Trivy reports zero critical CVEs in packages"),
        ("Trivy Vulnerability Scan on Frontend Filesystem", "dependencies", "critical", "Scan frontend directory with Trivy scanner", "Trivy reports zero critical CVEs in dependencies"),
        ("Trivy Config Scan for Misconfigurations", "dependencies", "high", "Scan repository configuration files with Trivy config", "No insecure file permissions or dangerous flags"),
        ("Trivy Secret Scanning in Repository", "secrets", "critical", "Scan entire git repository for committed secrets", "Zero API keys, passwords, or tokens found"),
        ("Gitleaks Scan for Hardcoded Secrets", "secrets", "critical", "Run Gitleaks on all commits and files", "Zero private keys, AWS tokens, or JWT secrets found"),
        ("Verification of .gitignore for Sensitive Files", "secrets", "high", "Verify .gitignore includes .env, *.db, *.log, certs", ".env and database credentials strictly excluded from git"),
        ("Absence of Hardcoded Secret Keys in config.py", "secrets", "critical", "Inspect app/config.py for hardcoded default secrets", "SECRET_KEY read from environment variable with secure fallback"),
        ("Absence of Database Passwords in Docker/Scripts", "secrets", "critical", "Inspect entrypoint.sh and script files", "No database passwords hardcoded in shell scripts"),
        ("Absence of Email API Keys in email_service.py", "secrets", "high", "Inspect email service configuration", "Sendinblue / SMTP keys loaded strictly from env"),
        ("License Compliance Audit on Python Dependencies", "dependencies", "low", "Audit licenses of Python requirements (MIT, Apache, BSD)", "All dependencies use permissible open-source licenses"),
        ("License Compliance Audit on Node Dependencies", "dependencies", "low", "Audit licenses in package-lock.json", "No restrictive GPL or proprietary license conflicts"),
        ("Outdated Dependency Security Check", "dependencies", "medium", "Check for deprecated or unmaintained packages", "Core dependencies maintained and receiving security updates"),
        ("Lockfile Integrity Verification (package-lock.json)", "dependencies", "high", "Verify npm lockfile integrity hashes match registry", "All package hashes verify without tampering"),
        ("Lockfile Integrity Verification (skills-lock.json)", "dependencies", "medium", "Inspect skills-lock.json integrity", "Lockfile adheres to expected schema"),
        ("Subresource Integrity (SRI) Check for Web Fonts", "dependencies", "low", "Inspect external font imports", "Fonts loaded securely over HTTPS or bundled locally"),
        ("Transitive Dependency Vulnerability Scan", "dependencies", "high", "Deep-scan nested dependency tree with pipdeptree", "No nested vulnerable packages undetected"),
        ("Phantom / Typo-squatting Package Name Audit", "dependencies", "medium", "Verify package names match official PyPI/npm packages", "All package names correspond to legitimate projects"),
        ("Direct Dependency Pinning Verification", "dependencies", "high", "Verify exact version pinning in requirements.txt", "Requirements pin exact semantic versions (==)"),
        ("Docker Base Image Security Assessment", "dependencies", "high", "Inspect Dockerfile base image if present", "Uses official slim/alpine minimal security image"),
        ("CI Dependency Cache Integrity Verification", "dependencies", "medium", "Verify CI cache keys include hash of lockfiles", "Cache invalidated immediately upon lockfile change"),
        ("Software Bill of Materials (SBOM) Generation", "dependencies", "medium", "Generate CycloneDX / SPDX SBOM report", "Valid SBOM generated covering all components"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(dep_defs, start=46):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 3. Static Code Analysis & SAST (Bandit / Semgrep) (SEC-086 - SEC-125) = 40
    sast_defs = [
        ("Bandit B101: Assert Statement Usage in Production", "sast", "low", "Scan Python codebase for assert statements in business logic", "No asserts used for critical validation"),
        ("Bandit B102: Exec Call Usage Audit", "sast", "critical", "Scan for dynamic code execution via exec()", "Zero occurrences of exec() in Python codebase"),
        ("Bandit B103: File Permissions Set to Insecure Mask", "sast", "medium", "Scan for chmod with world-writable permissions", "No insecure file permission modifications"),
        ("Bandit B104: Hardcoded Bind to 0.0.0.0", "sast", "low", "Check network socket bindings", "Configurable via environment variables"),
        ("Bandit B105: Hardcoded Password Strings in Code", "sast", "high", "Scan for hardcoded password variables", "No hardcoded plaintext password strings"),
        ("Bandit B106: Hardcoded Secret Key Assignment", "sast", "high", "Scan for literal secret key assignments", "Secrets loaded from settings/env"),
        ("Bandit B108: Insecure Temporary File Creation", "sast", "medium", "Scan for insecure /tmp file operations", "Uses secure tempfile modules where needed"),
        ("Bandit B301: Python Pickle Deserialization Flaw", "sast", "critical", "Scan for unsafe pickle.loads() usage", "Zero occurrences of pickle deserialization"),
        ("Bandit B302: Python Marshal Deserialization Flaw", "sast", "critical", "Scan for marshal.loads() usage", "Zero occurrences of marshal usage"),
        ("Bandit B303: Insecure MD5 / SHA1 Hash Algorithms", "sast", "high", "Scan for md5 or sha1 used for security/passwords", "Uses bcrypt / sha256; zero md5 for passwords"),
        ("Bandit B304: Insecure Cipher Usage (DES/RC4)", "sast", "critical", "Scan for obsolete cryptographic ciphers", "Zero legacy cipher usage"),
        ("Bandit B307: Unsafe Eval() Function Call", "sast", "critical", "Scan for eval() function calls", "Zero occurrences of eval() in codebase"),
        ("Bandit B310: Insecure urllib.urlopen Usage", "sast", "high", "Scan for unsafe URL open methods", "Uses requests/httpx with scheme verification"),
        ("Bandit B324: Hashlib Insecure Usage Without usedforsecurity", "sast", "low", "Inspect hashlib calls", "No insecure hashing in security contexts"),
        ("Bandit B602: Subprocess Call with shell=True", "sast", "critical", "Scan for subprocess.Popen/run with shell=True", "Zero occurrences of shell=True command injection risks"),
        ("Bandit B608: SQL Injection via String Concatenation", "sast", "critical", "Scan for raw SQL queries with string formatting", "All queries use SQLAlchemy ORM parameterized statements"),
        ("Bandit B701: Jinja2 Autoescape Configuration", "sast", "medium", "Scan template rendering configurations", "Autoescape enabled for all template contexts"),
        ("Bandit Full Repository Scan", "sast", "critical", "Execute full Bandit scan with -r backend/app", "Bandit reports zero High or Critical severity findings"),
        ("Semgrep Rule: FastAPI CORS Wildcard with Credentials", "sast", "critical", "Semgrep rule checking allow_origins=['*'] with allow_credentials=True", "CORS origins properly restricted"),
        ("Semgrep Rule: Raw SQL Execution in SQLAlchemy", "sast", "critical", "Semgrep rule scanning for text() with formatted strings", "Zero unparameterized SQL queries"),
        ("Semgrep Rule: Path Traversal in File Uploads", "sast", "critical", "Semgrep rule scanning for path traversal via filename", "Upload filenames sanitized/prefixed with random uuid"),
        ("Semgrep Rule: Hardcoded JWT Secret Key", "sast", "high", "Semgrep rule checking for hardcoded JWT secret", "JWT secret loaded from settings"),
        ("Semgrep Rule: Unhandled Exception Stack Trace Leak", "sast", "medium", "Semgrep rule scanning for exception str(e) leakage in 500", "Exceptions handled without leaking internal details"),
        ("Semgrep Rule: Insecure Random Number Generator for OTP", "sast", "high", "Semgrep rule scanning for random.randint used for crypto", "OTP entropy verified; secure random recommended"),
        ("Semgrep Rule: Missing Authentication Decorator on Admin", "sast", "critical", "Semgrep rule checking admin endpoints have role checks", "Admin endpoints verify current_user.role == 'Admin'"),
        ("Semgrep Rule: OAuth2 Password Form Insecure Scope", "sast", "low", "Semgrep rule checking OAuth2 form handling", "Complies with standard password flow"),
        ("Semgrep Rule: Insecure Deserialization in Pydantic", "sast", "medium", "Semgrep rule scanning for arbitrary type validation", "Pydantic models declare explicit typed schemas"),
        ("Semgrep Rule: Unvalidated Redirects in FastAPI", "sast", "medium", "Semgrep rule scanning for RedirectResponse with user input", "Zero unvalidated open redirects"),
        ("Semgrep Rule: React dangerouslySetInnerHTML Usage", "sast", "high", "Semgrep rule scanning frontend for dangerouslySetInnerHTML", "HTML tags sanitized; no unescaped user content"),
        ("Semgrep Rule: Next.js Server-Side Request Forgery", "sast", "high", "Semgrep rule scanning for fetch() with dynamic user URL", "Zero unvalidated server-side URL fetches"),
        ("Semgrep Rule: Prototype Pollution in JavaScript", "sast", "medium", "Semgrep rule scanning for Object.assign with untrusted input", "No prototype pollution vectors detected"),
        ("Semgrep Rule: Insecure Regular Expressions (ReDoS)", "sast", "medium", "Semgrep rule checking for catastrophic backtracking regex", "Regular expressions linear time bounded"),
        ("Semgrep Full Repository Scan", "sast", "critical", "Run Semgrep with p/security-audit ruleset", "Semgrep reports zero High/Critical security vulnerabilities"),
        ("ESLint Security Plugin Scan on Frontend", "sast", "medium", "Run eslint-plugin-security on Next.js frontend code", "Zero high severity security findings in frontend"),
        ("Check for Commented-out Secrets / Credentials", "sast", "medium", "Regex scan for comments like '# password = ...'", "Zero commented credentials in source files"),
        ("Check for Insecure HTTP URLs in Codebase", "sast", "low", "Scan codebase for hardcoded 'http://' URLs", "Only localhost/mock URLs use http; external APIs use https"),
        ("Database Connection String Security in alembic.ini", "sast", "high", "Inspect alembic.ini for hardcoded database passwords", "Alembic reads sqlalchemy.url from environment"),
        ("Check for Debug Mode Enabled in Production", "sast", "high", "Inspect config.py for DEBUG=True flags", "Debug mode disabled by default"),
        ("Check for Insecure File Extensions in Uploads", "sast", "high", "Scan upload handler for extension whitelisting", "Only CSV extensions allowed for data ingestion"),
        ("Static Code Security Assessment Summary", "sast", "critical", "Compile combined Bandit + Semgrep SAST score", "SAST compliance 100% with all rules passing"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(sast_defs, start=86):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 4. Authentication & Authorization Security (SEC-126 - SEC-175) = 50
    auth_sec_defs = [
        ("JWT Algorithm Confusion Defense (None Algorithm)", "auth", "critical", "Submit JWT token with 'alg': 'none'", "Token rejected with 401 Unauthorized"),
        ("JWT Algorithm Confusion Defense (RS256 vs HS256)", "auth", "critical", "Submit HMAC-signed token against RSA public key endpoint", "Rejected due to algorithm mismatch"),
        ("JWT Signature Tampering Defense", "auth", "critical", "Alter payload in valid JWT without re-signing", "Rejected due to invalid cryptographic signature"),
        ("JWT Expiration (exp) Claim Enforcement", "auth", "critical", "Submit expired JWT token (exp in past)", "Rejected with 401 'Token expired'"),
        ("JWT Not Before (nbf) Claim Enforcement", "auth", "high", "Submit JWT with nbf timestamp in future", "Rejected with 401 'Token not yet valid'"),
        ("JWT Missing Subject (sub) Claim Handling", "auth", "high", "Submit JWT token omitting 'sub' username claim", "Rejected with 401 'Could not validate credentials'"),
        ("JWT Weak Secret Key Brute Force Resistance", "auth", "critical", "Test if JWT secret key can be cracked via wordlist", "Secret key has sufficient entropy (> 256 bits)"),
        ("Password Hashing Algorithm Verification", "auth", "critical", "Inspect stored password_hash column in User table", "Passwords hashed using bcrypt with work factor >= 12"),
        ("Absence of Plaintext Passwords in DB / Logs", "auth", "critical", "Inspect database and server logs during login", "Zero plaintext passwords logged or persisted"),
        ("Password Complexity Policy Enforcement (Length)", "auth", "high", "Attempt to register with password of 7 characters", "Rejected with 400 'Password must be at least 8 characters'"),
        ("Password Complexity Policy Enforcement (Uppercase)", "auth", "medium", "Attempt to register without uppercase character", "Rejected with 400 'Password must contain uppercase letter'"),
        ("Password Complexity Policy Enforcement (Digits)", "auth", "medium", "Attempt to register without numeric digits", "Rejected with 400 'Password must contain at least one number'"),
        ("Password Complexity Policy Enforcement (Special Chars)", "auth", "medium", "Attempt to register without special character", "Rejected with 400 'Password must contain special character'"),
        ("User Enumeration Defense on Login Endpoint", "auth", "high", "Compare response times and messages for valid vs invalid user", "Returns identical 'Incorrect username or password' in similar time"),
        ("User Enumeration Defense on Forgot Password", "auth", "high", "Submit non-existent email to /api/v1/auth/forgot-password", "Returns identical generic success message to prevent user probing"),
        ("OTP Code Entropy & Randomness Verification", "auth", "high", "Verify OTP generation code in auth.py", "Generates 6-digit cryptographic code (100000 - 999999)"),
        ("OTP Code Expiration Enforcement", "auth", "high", "Attempt to use OTP after expiration window", "Rejected with 400 'Invalid or expired OTP'"),
        ("OTP Single-Use Enforcement (Replay Attack Defense)", "auth", "critical", "Attempt to reuse valid OTP twice for password reset", "Second attempt fails as verification_code cleared to None"),
        ("OTP Brute Force Rate Limiting", "auth", "high", "Submit 100 rapid incorrect OTP guesses", "Requests rate limited to prevent brute forcing 6-digit codes"),
        ("Account Takeover via Parameter Tampering on Reset", "auth", "critical", "Submit password reset specifying different email in body", "Cannot reset password of another user without their OTP"),
        ("IDOR Defense on /api/v1/auth/me Endpoint", "auth", "critical", "Attempt to fetch another user profile by tampering params", "Endpoint extracts identity strictly from verified JWT subject"),
        ("RBAC: Researcher Role Access to Admin Overview", "auth", "critical", "Send GET /api/v1/admin/overview with Researcher JWT", "HTTP 403 Forbidden 'Admin access required'"),
        ("RBAC: Researcher Role Access to Admin Profile Update", "auth", "critical", "Send PUT /api/v1/admin/profile with Researcher JWT", "HTTP 403 Forbidden 'Admin access required'"),
        ("RBAC: Unauthenticated Access to Admin Overview", "auth", "critical", "Send GET /api/v1/admin/overview without Authorization header", "HTTP 401 Unauthorized 'Not authenticated'"),
        ("RBAC: Unauthenticated Access to /auth/me", "auth", "critical", "Send GET /api/v1/auth/me without token", "HTTP 401 Unauthorized 'Not authenticated'"),
        ("Privilege Escalation via Registration Body Role Injection", "auth", "critical", "Submit role='Admin' inside registration request payload", "Server ignores role in body; assigns Researcher (or Admin only if user_count==0)"),
        ("Privilege Escalation via JWT Role Claim Tampering", "auth", "critical", "Sign custom JWT with role='Admin' using wrong key", "Rejected due to invalid signature"),
        ("Unauthorized Favorite Gene Mutation", "auth", "high", "Send POST /api/v1/genes/{id}/favorite without token", "HTTP 401 Unauthorized 'Authentication required'"),
        ("Unauthorized Favorite Gene Deletion", "auth", "high", "Send DELETE /api/v1/genes/{id}/favorite without token", "HTTP 401 Unauthorized 'Authentication required'"),
        ("IDOR on Favorite Gene: Delete Other User's Favorite", "auth", "high", "Attempt to delete favorite belonging to different user", "Endpoint restricts deletion to current_user.user_id"),
        ("Clear Stuck User Endpoint Access Controls", "auth", "medium", "Audit access permissions on /clear-stuck-user", "Cleanup restricted or audited"),
        ("Session Invalidation on Password Change", "auth", "high", "Verify previously issued JWT behavior after password reset", "Password hash change prevents continued unauthorized session"),
        ("Concurrent Session Handling Security", "auth", "low", "Inspect simultaneous active sessions for user", "Handles multiple sessions safely"),
        ("Session Fixation Attack Defense", "auth", "high", "Verify new token generated upon authentication", "Fresh JWT token issued upon every successful login"),
        ("Bearer Token Format Compliance", "auth", "medium", "Submit token with scheme 'Basic' or 'Token' instead of 'Bearer'", "FastAPI OAuth2 rejects unsupported auth scheme"),
        ("Empty Bearer Token Handling", "auth", "low", "Submit 'Authorization: Bearer ' with empty string", "HTTP 401 returned immediately"),
        ("Authorization Header Injection / Line Folding", "auth", "medium", "Inject CRLF characters into Authorization header", "Rejected as invalid HTTP header"),
        ("Username Case Sensitivity & Normalization", "auth", "medium", "Register 'Researcher1' and attempt 'researcher1'", "Properly handles case collisions and normalization"),
        ("Email Case Normalization in Registration", "auth", "medium", "Register with uppercase email 'USER@DOMAIN.COM'", "Email normalized preventing duplicate accounts"),
        ("Email Regex Validation Conformance", "auth", "medium", "Submit malformed emails to registration endpoint", "email-validator rejects invalid syntax"),
        ("OAuth2 Content-Type Enforcement", "auth", "low", "Send JSON body to /api/v1/auth/login", "FastAPI requires application/x-www-form-urlencoded"),
        ("OAuth2 Scope Enforcement", "auth", "low", "Inspect requested scopes in token generation", "Scopes validated according to role capabilities"),
        ("Password Hash Timing Attack Resistance", "auth", "high", "Measure execution time of passlib verify_password", "Bcrypt constant-time verification protects against timing attacks"),
        ("Default Admin Account Credentials Audit", "auth", "critical", "Verify no default admin/admin accounts in database seeds", "Seeds require explicit setup; no default hardcoded passwords"),
        ("SQL Injection via Login Username Field", "auth", "critical", "Submit \"' OR 1=1 --\" in login username input", "SQLAlchemy parameterized query treats input as literal string; login fails safely"),
        ("SQL Injection via Login Password Field", "auth", "critical", "Submit SQL injection payload in password field", "Password compared via bcrypt against hashed value; zero SQL execution"),
        ("Admin Update Profile Target Verification", "auth", "high", "Verify PUT /admin/profile updates only the calling admin", "db.merge(current_user) modifies only authenticated user"),
        ("User Email Verification Flag Integrity", "auth", "medium", "Check email_verified state assignment", "Set according to business logic"),
        ("Registration Rate Limiting / DoS Defense", "auth", "high", "Submit 1,000 rapid user registrations", "Rate limiting restricts automated account flooding"),
        ("Comprehensive Authentication Security Audit", "auth", "critical", "Evaluate complete authentication and RBAC attack surface", "All OWASP ASVS Level 2 authentication controls satisfied"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(auth_sec_defs, start=126):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 5. Input Validation, Injection Defense & API Security (SEC-176 - SEC-240) = 65
    input_sec_defs = [
        ("SQL Injection Defense: Search Query 'q' Parameter", "injection", "critical", "Send GET /api/v1/search?q=1'%20OR%20'1'='1", "SQLAlchemy parameterizes query; returns zero or valid matches without SQL error"),
        ("SQL Injection Defense: Search Union Based Exploit", "injection", "critical", "Send GET /api/v1/search?q=' UNION SELECT 1,username,password_hash FROM users--", "Query treated as search text; no data leakage"),
        ("SQL Injection Defense: Search Time-Based Blind Exploit", "injection", "critical", "Send GET /api/v1/search?q=BRCA1' AND (SELECT 1 FROM (SELECT(SLEEP(5)))a)--", "Query finishes without delay; sleep command not executed"),
        ("SQL Injection Defense: Gene Chromosome Filter", "injection", "critical", "Send GET /api/v1/genes?chromosome=1'%20OR%201=1--", "Filter treated as literal chromosome string; no data leak"),
        ("SQL Injection Defense: Gene ID Path Parameter", "injection", "critical", "Send GET /api/v1/genes/BRCA1'%20OR%20'1'='1", "Returns 404 Gene not found; zero SQL error"),
        ("SQL Injection Defense: Disease ID Path Parameter", "injection", "critical", "Send GET /api/v1/diseases/DIS001'%20OR%20'1'='1", "Returns 404 Disease not found"),
        ("SQL Injection Defense: Variant Mutation Type Filter", "injection", "high", "Send GET /api/v1/variants?mutation_type=' OR 1=1--", "Treated as literal filter string"),
        ("SQL Injection Defense: Variant Clinical Significance Filter", "injection", "high", "Send GET /api/v1/variants?clinical_significance=' OR 1=1--", "Treated as literal filter string"),
        ("SQL Injection Defense: Association Evidence Level Filter", "injection", "high", "Send GET /api/v1/associations?evidence_level=' OR 1=1--", "Treated as literal filter string"),
        ("SQL Injection Defense: Stats Endpoint SQL Group-By", "injection", "high", "Inspect SQL aggregation queries in get_stats()", "Aggregations use ORM models (func.count) safely"),
        ("SQL Injection Defense: Clear Stuck User Email Param", "injection", "critical", "Send DELETE /api/v1/auth/clear-stuck-user?email=' OR 1=1--", "Filters by literal email without deleting entire table"),
        ("XSS Defense: Stored XSS in User Registration Username", "xss", "critical", "Register username '<script>alert(document.cookie)</script>'", "Characters escaped in responses; script does not execute in browser"),
        ("XSS Defense: Stored XSS in User Registration Email", "xss", "high", "Register email with script tags", "Rejected by email format validation"),
        ("XSS Defense: Stored XSS in Admin Profile Update", "xss", "high", "Update admin username to '<img src=x onerror=alert(1)>'", "Payload escaped on render in UI components"),
        ("XSS Defense: Reflected XSS in Search Query Parameter", "xss", "critical", "Send GET /api/v1/search?q=<script>alert('XSS')</script>", "Frontend escapes search snippet; HTML entities encoded"),
        ("XSS Defense: Reflected XSS in Search Highlighting Tags", "xss", "high", "Inspect pre_tags and post_tags in search highlight", "Highlight tags use controlled CSS classes without script execution"),
        ("XSS Defense: Reflected XSS in 404 Error Detail Messages", "xss", "medium", "Navigate to /api/v1/genes/<svg/onload=alert(1)>", "404 detail returned as JSON string without HTML rendering"),
        ("XSS Defense: Reflected XSS in URL Fragment / Hash", "xss", "medium", "Navigate to frontend URL with #<script>alert(1)</script>", "React/Next.js sanitizes router query and hash parameters"),
        ("DOM-based XSS Defense in D3 / Plotly Renderers", "xss", "medium", "Pass XSS payload into chart label attributes", "Plotly / D3 render text safely without innerHTML exploitation"),
        ("Path Traversal Defense: Uploaded Files Directory", "traversal", "critical", "Request /backend/uploads/../../../../etc/passwd", "Path traversal rejected or blocked by static file handler"),
        ("Path Traversal Defense: File Ingestion Script", "traversal", "critical", "Attempt file upload with filename '../../secret.txt'", "Filename sanitized; directory traversal blocked"),
        ("CSV Formula Injection Defense (CSV Injection)", "injection", "high", "Upload CSV containing cells '=cmd|' /C calc'!A0'", "Cell formulas sanitized or prefixed with quote when exported"),
        ("CSV Ingestion Malformed Header Handling", "input-validation", "medium", "Upload CSV missing required schema columns", "Ingestion rejects file with 400 validation error"),
        ("CSV Ingestion File Size Limitation", "dos", "high", "Attempt to upload 500MB file to uploads directory", "Server rejects payload exceeding maximum body size (413 Payload Too Large)"),
        ("CSV Ingestion Empty File Handling", "input-validation", "low", "Upload 0-byte CSV file", "Ingestion rejects empty file gracefully"),
        ("CSV Ingestion Non-CSV File Type Rejection", "input-validation", "medium", "Upload executable .exe renamed to .csv", "MIME type and file header validation rejects non-text files"),
        ("JSON Deserialization Bomb Defense (Deep Nesting)", "dos", "medium", "Send JSON payload with 1,000 levels of nested objects", "FastAPI parser rejects deeply nested payloads preventing stack overflow"),
        ("JSON Payload Size Limit Enforcement", "dos", "medium", "Send 50MB JSON payload to registration endpoint", "Server rejects oversized request body with 413"),
        ("Query Parameter Integer Overflow Defense", "input-validation", "medium", "Send GET /api/v1/genes?skip=99999999999999999999999", "FastAPI Pydantic validates integer range; returns 422"),
        ("Negative Integer Parameter Handling", "input-validation", "medium", "Send GET /api/v1/genes?limit=-10&skip=-5", "FastAPI validates non-negative integers; returns 422"),
        ("Excessive Pagination Limit Parameter Handling", "dos", "high", "Send GET /api/v1/genes?limit=10000000", "Server caps maximum limit parameter to prevent memory exhaustion"),
        ("HTTP Method Tampering Defense (HEAD, TRACE, TRACK)", "api", "medium", "Send HTTP TRACE request to API endpoints", "HTTP 405 Method Not Allowed; TRACE debugging disabled"),
        ("HTTP Verb Tampering: POST Endpoint via GET", "api", "low", "Send GET to POST-only /api/v1/auth/register", "HTTP 405 Method Not Allowed"),
        ("HTTP Verb Tampering: DELETE Endpoint via GET", "api", "low", "Send GET to DELETE /api/v1/genes/{id}/favorite", "HTTP 405 Method Not Allowed"),
        ("Content-Type Header Spoofing Defense", "api", "medium", "Send XML payload with 'Content-Type: application/json'", "Pydantic JSON parser fails gracefully with 422"),
        ("Missing Content-Type Header on POST Requests", "api", "low", "Send POST request omitting Content-Type header", "FastAPI returns 422 Unprocessable Entity"),
        ("Host Header Injection Defense", "api", "high", "Send request with forged Host: evil-phishing.com", "Server rejects or ignores untrusted host headers"),
        ("Server-Side Request Forgery (SSRF) Defense in Email Service", "api", "critical", "Verify email service does not accept arbitrary webhook URLs", "Email dispatched strictly to configured SMTP / Brevo servers"),
        ("Elasticsearch Query Injection Defense", "injection", "critical", "Send crafted Elasticsearch bool/match payload in search", "Query sanitized before submitting to Elasticsearch multi_match"),
        ("Elasticsearch Denial-of-Service Fuzzing", "dos", "medium", "Send wildcard regex query '*.*' to search", "Query execution bounded by timeout and fuzzy limits"),
        ("Information Disclosure in 500 Error Responses", "info-leak", "critical", "Trigger unexpected exception on server", "Response returns generic 500 error; zero Python tracebacks exposed"),
        ("Information Disclosure in Database Error Responses", "info-leak", "high", "Trigger database constraint violation", "Response returns sanitized 400 error; zero raw SQL strings exposed"),
        ("Internal IP Address Disclosure in Headers/Body", "info-leak", "medium", "Audit response bodies and headers for private 10.x/192.168.x IPs", "Zero internal infrastructure IP addresses exposed"),
        ("Source Code Disclosure via .git / Backup Files", "info-leak", "high", "Attempt GET /.git/config and GET /app.db.bak", "HTTP 404 returned; sensitive source files blocked"),
        ("Database File Direct Download Block", "info-leak", "critical", "Attempt direct GET /disease_gene_map.db or /app.db", "HTTP 404 returned; database files not served by web server"),
        ("Environment File Direct Download Block", "info-leak", "critical", "Attempt direct GET /.env or GET /.env.example", "Static server rejects hidden and dot-files"),
        ("Log File Direct Download Block", "info-leak", "critical", "Attempt direct GET /etl_ingestion.log", "Log files not accessible via HTTP endpoints"),
        ("OpenAPI Documentation Access Controls", "info-leak", "low", "Verify OpenAPI schema does not expose secret keys or passwords", "Schema defines data models without exposing credentials"),
        ("Rate Limiting on Search Endpoint", "dos", "high", "Send 500 rapid search requests per second", "Rate limiting protects search engine from resource exhaustion"),
        ("Rate Limiting on Stats Endpoint", "dos", "medium", "Send rapid requests to computationally heavy /stats", "Heavy aggregation queries throttled"),
        ("CORS Wildcard with Preflight Verification", "api", "high", "Verify allowed origins match trusted frontend domains", "Origins configured via settings.BACKEND_CORS_ORIGINS"),
        ("CORS Null Origin Handling", "api", "high", "Send request with 'Origin: null'", "Rejected; null origin not permitted access"),
        ("CORS Subdomain Takeover Defense", "api", "medium", "Send request with 'Origin: attacker.diseasegenemap.com'", "Only explicitly trusted domain names allowed"),
        ("JSON Parsing Prototype Pollution in Backend", "api", "low", "Send JSON with '__proto__' keys to API endpoints", "Pydantic parses into strongly typed Python objects without pollution"),
        ("Unicode Normalization Vulnerability Defense", "input-validation", "medium", "Send homoglyph / visual spoofing characters in usernames", "Strings normalized properly before database query"),
        ("Null Byte Injection Defense in File Paths", "injection", "high", "Send filename containing '%00.csv'", "Null bytes rejected by file handler"),
        ("HTTP Parameter Pollution (HPP) Defense", "input-validation", "medium", "Send duplicate parameters '?q=val1&q=val2'", "FastAPI handles list or uses first value consistently"),
        ("XML External Entity (XXE) Injection Defense", "injection", "critical", "Submit XML payload with DOCTYPE entity definition", "XML parsing disabled; application accepts only JSON"),
        ("Mass Assignment Vulnerability Defense in User Registration", "api", "critical", "Include unmapped fields like is_superuser=True in registration", "Pydantic UserCreate strictly filters fields; extra keys ignored"),
        ("Mass Assignment Defense in Admin Profile Update", "api", "critical", "Include role='SuperAdmin' in UpdateProfileRequest", "UpdateProfileRequest accepts strictly username and email"),
        ("Session Expiry Token Revocation Check", "auth", "high", "Attempt to access API with expired token after logout", "Request rejected with 401 Unauthorized"),
        ("Unauthenticated Download of Exported CSV Data", "auth", "medium", "Attempt to download database export without credentials", "Export endpoints require valid user session"),
        ("Slowloris HTTP Denial-of-Service Defense", "dos", "high", "Send incomplete HTTP headers slowly to server", "Uvicorn connection timeout drops stalled connections"),
        ("HTTP Request Smuggling Defense", "api", "critical", "Send conflicting Content-Length and Transfer-Encoding headers", "Uvicorn/ASGI server rejects ambiguous smuggling headers"),
        ("Comprehensive API Security SLA Verification", "api", "critical", "Audit entire API against OWASP API Security Top 10 2023", "All 10 risk categories mitigated with automated controls"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(input_sec_defs, start=176):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    # 6. OWASP ZAP Baseline & Dynamic Scanning (SEC-241 - SEC-300) = 60
    zap_defs = [
        ("ZAP Passive Scan: Directory Browsing Enabled", "zap", "high", "ZAP passive rule 10015 scanning directory listings", "Directory browsing disabled across all web directories"),
        ("ZAP Passive Scan: Cross-Domain Misconfiguration", "zap", "medium", "ZAP passive rule 10098 scanning crossdomain.xml", "No insecure cross-domain policy files hosted"),
        ("ZAP Passive Scan: Vulnerable JS Library Detection", "zap", "high", "ZAP passive rule 10003 scanning client JS libraries", "All bundled JS libraries free from known Retire.js CVEs"),
        ("ZAP Passive Scan: Insecure Cookie Without HttpOnly", "zap", "high", "ZAP passive rule 10010 scanning Set-Cookie headers", "Zero authentication cookies missing HttpOnly flag"),
        ("ZAP Passive Scan: Insecure Cookie Without Secure Flag", "zap", "high", "ZAP passive rule 10011 scanning Set-Cookie headers", "Zero sensitive cookies missing Secure flag"),
        ("ZAP Passive Scan: Insecure Cookie Without SameSite", "zap", "high", "ZAP passive rule 10054 scanning Set-Cookie SameSite", "All cookies specify SameSite attribute"),
        ("ZAP Passive Scan: Password Autocomplete in HTML", "zap", "low", "ZAP passive rule 10025 scanning form inputs", "Password fields configure autocomplete='current-password'/'new-password'"),
        ("ZAP Passive Scan: Private IP Address Disclosure", "zap", "medium", "ZAP passive rule 10037 scanning response text", "Zero internal IPv4/IPv6 private addresses leaked"),
        ("ZAP Passive Scan: Session ID in URL Rewrite", "zap", "high", "ZAP passive rule 10043 scanning URL parameters", "Zero session tokens or JWTs transmitted in URL query strings"),
        ("ZAP Passive Scan: Script Active Content in SVG", "zap", "medium", "ZAP passive rule 10044 scanning SVG images", "Zero executable JavaScript in image assets"),
        ("ZAP Passive Scan: Source Code Disclosure in Comments", "zap", "low", "ZAP passive rule 10027 scanning HTML comments", "Zero sensitive SQL, credentials, or internal paths in HTML comments"),
        ("ZAP Passive Scan: Missing Anti-Clickjacking Header", "zap", "high", "ZAP passive rule 10020 scanning X-Frame-Options/CSP", "Clickjacking protection present on all rendered pages"),
        ("ZAP Passive Scan: X-Content-Type-Options Missing", "zap", "medium", "ZAP passive rule 10021 scanning nosniff header", "nosniff header present on all API and asset responses"),
        ("ZAP Passive Scan: Content-Security-Policy Missing", "zap", "high", "ZAP passive rule 10038 scanning CSP header", "CSP header deployed across web application routes"),
        ("ZAP Passive Scan: Strict-Transport-Security Missing", "zap", "high", "ZAP passive rule 10035 scanning HSTS header", "HSTS header present with valid duration on HTTPS"),
        ("ZAP Passive Scan: Server Information Leak via Server Header", "zap", "low", "ZAP passive rule 10036 scanning Server banner", "Server banner minimized or suppressed"),
        ("ZAP Passive Scan: Timestamp Disclosure in Responses", "zap", "low", "ZAP passive rule 10096 scanning UNIX timestamps", "Timestamps do not expose server system clock offsets"),
        ("ZAP Passive Scan: Weak Hash Algorithm in Signature", "zap", "high", "ZAP rule inspecting TLS certificate signatures", "SHA-256 or stronger signature algorithm used"),
        ("ZAP Passive Scan: Anti-CSRF Tokens on Forms", "zap", "high", "ZAP passive rule 10202 scanning POST forms", "State-changing actions protected by Bearer auth / CSRF tokens"),
        ("ZAP Passive Scan: Information Disclosure - Debug Errors", "zap", "high", "ZAP passive rule 10023 scanning HTTP 500 pages", "Zero stack traces or debug pages exposed in production"),
        ("ZAP Spider: Application Endpoint Discovery", "zap", "medium", "Run ZAP spider crawler on DiseaseGene routes", "Discovers all public routes: /genes, /diseases, /variants, /search"),
        ("ZAP Spider: API OpenAPI Spec Ingestion", "zap", "high", "Import /api/v1/openapi.json into ZAP API catalog", "All REST API endpoints successfully cataloged for inspection"),
        ("ZAP Baseline Scan on Root Endpoint /", "zap", "critical", "Execute ZAP baseline scan on root path", "Zero high or medium severity baseline alert findings"),
        ("ZAP Baseline Scan on /health Endpoint", "zap", "medium", "Execute ZAP baseline scan on health route", "Zero security alerts on health endpoint"),
        ("ZAP Baseline Scan on /api/v1/stats Endpoint", "zap", "high", "Execute ZAP baseline scan on stats route", "Zero security alerts; data delivered securely"),
        ("ZAP Baseline Scan on /genes Endpoint", "zap", "high", "Execute ZAP baseline scan on genes catalog", "Zero security alerts; pagination parameters secure"),
        ("ZAP Baseline Scan on /diseases Endpoint", "zap", "high", "Execute ZAP baseline scan on diseases catalog", "Zero security alerts on disease endpoints"),
        ("ZAP Baseline Scan on /variants Endpoint", "zap", "high", "Execute ZAP baseline scan on variants catalog", "Zero security alerts on variants endpoints"),
        ("ZAP Baseline Scan on /pathways Endpoint", "zap", "medium", "Execute ZAP baseline scan on pathways catalog", "Zero security alerts on pathways endpoints"),
        ("ZAP Baseline Scan on /associations Endpoint", "zap", "high", "Execute ZAP baseline scan on associations catalog", "Zero security alerts on association endpoints"),
        ("ZAP Baseline Scan on /drugs Endpoint", "zap", "medium", "Execute ZAP baseline scan on drugs catalog", "Zero security alerts on drugs endpoints"),
        ("ZAP Baseline Scan on /publications Endpoint", "zap", "medium", "Execute ZAP baseline scan on publications catalog", "Zero security alerts on publication endpoints"),
        ("ZAP Baseline Scan on /search Endpoint", "zap", "critical", "Execute ZAP baseline scan on search route", "Zero security alerts; query input properly handled"),
        ("ZAP Baseline Scan on /auth/login Endpoint", "zap", "critical", "Execute ZAP baseline scan on authentication endpoint", "Zero security alerts; credentials protected in transit"),
        ("ZAP Baseline Scan on /auth/register Endpoint", "zap", "critical", "Execute ZAP baseline scan on registration endpoint", "Zero security alerts; inputs validated"),
        ("ZAP Baseline Scan on /auth/forgot-password", "zap", "high", "Execute ZAP baseline scan on forgot-password route", "Zero security alerts; rate limiting and generic responses verified"),
        ("ZAP Baseline Scan on /admin/overview Endpoint", "zap", "critical", "Execute ZAP baseline scan on admin route with auth", "Zero security alerts; authorization barriers verified"),
        ("ZAP Passive Rule: Open Redirect Detection", "zap", "high", "ZAP passive rule scanning redirect query params", "Zero open redirect vulnerabilities detected"),
        ("ZAP Passive Rule: Insecure Content Inclusion over HTTP", "zap", "high", "ZAP rule scanning for mixed content resources", "Zero insecure HTTP resources loaded on HTTPS pages"),
        ("ZAP Passive Rule: Hash Disclosure in Web Content", "zap", "medium", "ZAP rule scanning for leaked MD5/SHA hashes", "Zero internal password or secret hashes exposed"),
        ("ZAP Passive Rule: Heartbleed Vulnerability Check", "zap", "critical", "Verify OpenSSL version resistant to Heartbleed", "Target server TLS stack secure against CVE-2014-0160"),
        ("ZAP Passive Rule: POODLE Vulnerability Check", "zap", "critical", "Verify SSL 3.0 disabled to prevent POODLE attack", "Target server TLS stack secure against CVE-2014-3566"),
        ("ZAP Passive Rule: Log4j / JNDI Injection Check", "zap", "critical", "Verify no vulnerable Java logging components", "Python/Node stack immune to CVE-2021-44228"),
        ("ZAP Passive Rule: Modern JS Framework Security", "zap", "medium", "Audit Next.js / React client bundles", "Client scripts free from known framework vulnerabilities"),
        ("ZAP Report HTML Generation Verification", "zap", "high", "Verify ZAP generates zap-report.html artifact", "HTML report successfully compiled with executive summary"),
        ("ZAP Report JSON Generation Verification", "zap", "high", "Verify ZAP generates zap-report.json machine-readable artifact", "JSON report compiled with alert counts and URLs"),
        ("ZAP Report SARIF Format Compatibility", "zap", "medium", "Verify ZAP report conversion to SARIF format", "Valid SARIF output generated for GitHub Code Scanning tab"),
        ("ZAP Scan Pass / Fail Policy Enforcement", "zap", "critical", "Enforce CI failure if High or Medium alerts found", "Zero High and Medium alerts allowed in CI build pipeline"),
        ("ZAP Scan Execution Duration Benchmark (< 3m)", "zap", "medium", "Measure ZAP baseline scan execution duration", "Scan completes within 3 minutes on standard CI runner"),
        ("ZAP Alert False Positive Suppression Configuration", "zap", "low", "Inspect zap-rules.conf suppression configuration", "False positive rules tuned appropriately without hiding real flaws"),
        ("ZAP Passive Scan on Web Application Assets", "zap", "low", "Scan CSS and image assets served by frontend", "Static assets served with appropriate security headers"),
        ("ZAP Automated Spider Depth Restriction", "zap", "medium", "Verify spider depth bounded to prevent infinite crawling", "Spider depth configured to 3 levels"),
        ("ZAP API Request Rate Throttling", "zap", "low", "Verify request rate limited to avoid target overload", "Scanner runs at safe 20 requests per second"),
        ("ZAP Authentication Context Configuration", "zap", "medium", "Verify ZAP bearer token auth script support", "Authenticated scanning executes cleanly with test token"),
        ("ZAP Non-Destructive Scanning Policy Verification", "zap", "critical", "Verify no destructive fuzzing or database DROP executed", "Scan strictly limited to safe passive and baseline rules"),
        ("ZAP Session State Preservation", "zap", "low", "Verify scan session saved for audit trail", "ZAP session state exported to artifacts"),
        ("ZAP CI Exit Code Mapping", "zap", "high", "Verify ZAP CLI returns exit code 0 when within thresholds", "Returns exit code 0 for clean builds, exit code 1 for violations"),
        ("ZAP Vulnerability Remediation Guide Verification", "zap", "medium", "Verify generated findings include remediation instructions", "Each finding includes Solution, Reference, and CWE ID"),
        ("ZAP Security Scan Step Summary Generator", "zap", "high", "Verify ZAP summary formatted for $GITHUB_STEP_SUMMARY", "Concise markdown table of alerts rendered in GitHub Actions summary"),
        ("Final Comprehensive 300-Test Security Suite Sign-off", "security", "critical", "Verify all 300 security tests pass defensive requirements", "Application achieves 100% security baseline compliance"),
    ]
    for i, (name, cat, prio, desc, exp) in enumerate(zap_defs, start=241):
        cases.append({"id": f"SEC-{i:03d}", "category": cat, "name": name, "priority": prio, "description": desc, "expected_result": exp})

    return cases


def main():
    print("Generating 1,200 unique test cases for DiseaseGeneMap...")
    
    # 1. Selenium
    sel_cases = generate_selenium_cases()
    sel_path = Path("tests/selenium/test_cases/test_cases.yml")
    sel_path.parent.mkdir(parents=True, exist_ok=True)
    with open(sel_path, "w", encoding="utf-8") as f:
        yaml.dump({"test_cases": sel_cases}, f, sort_keys=False, allow_unicode=True)
    print(f"  [+] Selenium: wrote {len(sel_cases)} test cases to {sel_path}")
    
    # 2. Appium
    app_cases = generate_appium_cases()
    app_path = Path("tests/appium/test_cases/test_cases.yml")
    app_path.parent.mkdir(parents=True, exist_ok=True)
    with open(app_path, "w", encoding="utf-8") as f:
        yaml.dump({"test_cases": app_cases}, f, sort_keys=False, allow_unicode=True)
    print(f"  [+] Appium: wrote {len(app_cases)} test cases to {app_path}")
    
    # 3. Load
    load_cases = generate_load_cases()
    load_path = Path("tests/load/test_cases/test_cases.yml")
    load_path.parent.mkdir(parents=True, exist_ok=True)
    with open(load_path, "w", encoding="utf-8") as f:
        yaml.dump({"test_cases": load_cases}, f, sort_keys=False, allow_unicode=True)
    print(f"  [+] k6 Load: wrote {len(load_cases)} test cases to {load_path}")
    
    # 4. Security
    sec_cases = generate_security_cases()
    sec_path = Path("tests/security/test_cases/test_cases.yml")
    sec_path.parent.mkdir(parents=True, exist_ok=True)
    with open(sec_path, "w", encoding="utf-8") as f:
        yaml.dump({"test_cases": sec_cases}, f, sort_keys=False, allow_unicode=True)
    print(f"  [+] Security: wrote {len(sec_cases)} test cases to {sec_path}")
    
    total = len(sel_cases) + len(app_cases) + len(load_cases) + len(sec_cases)
    print(f"Total test cases generated: {total} / 1200")

if __name__ == "__main__":
    main()
