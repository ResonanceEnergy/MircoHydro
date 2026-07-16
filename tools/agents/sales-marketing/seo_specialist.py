"""
SEO SPECIALIST AGENT
Keyword research, on-page optimization, technical SEO, and ranking strategies.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv(dotenv_path='../.env')

# Initialize Groq client
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

def keyword_research(topic):
    """
    Generate comprehensive keyword research and strategy.
    """
    
    prompt = f"""You are an SEO specialist doing keyword research for: {topic}

**KEYWORD RESEARCH REPORT**

---

**PRIMARY KEYWORDS** (High volume, high intent):

| Keyword | Search Volume | Competition | CPC | Intent | Priority |
|---------|---------------|-------------|-----|--------|----------|
| [keyword 1] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | High |
| [keyword 2] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | High |
| [keyword 3] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | High |

**Strategy**: Target these with dedicated landing pages, cornerstone content, product pages

---

**SECONDARY KEYWORDS** (Medium volume, good intent):

| Keyword | Search Volume | Competition | CPC | Intent | Priority |
|---------|---------------|-------------|-----|--------|----------|
| [keyword 4] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | Medium |
| [keyword 5] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | Medium |
| [keyword 6] | [X]k/month | Low/Med/High | $X.XX | Commercial/Informational | Medium |

**Strategy**: Target with supporting blog posts, category pages, resource pages

---

**LONG-TAIL KEYWORDS** (Lower volume, high conversion):

| Keyword | Search Volume | Competition | CPC | Intent | Priority |
|---------|---------------|-------------|-----|--------|----------|
| [long-tail 1] | [X]/month | Low | $X.XX | Transactional | High |
| [long-tail 2] | [X]/month | Low | $X.XX | Transactional | High |
| [long-tail 3] | [X]/month | Low | $X.XX | Transactional | High |

**Strategy**: Target with specific how-to guides, comparison pages, FAQ content

---

**QUESTION KEYWORDS** (People also ask, voice search):

1. "How does [topic] work?"
2. "What is the cost of [topic]?"
3. "How much [topic] do I need?"
4. "Where can I buy [topic]?"
5. "Is [topic] worth it?"
6. "What are the benefits of [topic]?"
7. "How to install [topic]?"
8. "How long does [topic] last?"
9. "[Topic] vs [alternative]?"
10. "Best [topic] for [use case]?"

**Strategy**: Create FAQ page, write blog posts answering each question, optimize for featured snippets

---

**LOCAL KEYWORDS** (If applicable):

- "[topic] near me" - [Volume]
- "[topic] in [city/state]" - [Volume]
- "[topic] contractors [location]" - [Volume]
- "best [topic] company [location]" - [Volume]

**Strategy**: Optimize Google Business Profile, create location pages, get local backlinks

---

**COMPETITOR KEYWORD GAP ANALYSIS**:

**Competitor 1**: [Competitor Name]
- Keywords they rank for that we don't: [List top 10]
- Opportunity: [Which to target first]

**Competitor 2**: [Competitor Name]
- Keywords they rank for that we don't: [List top 10]
- Opportunity: [Which to target first]

**Competitor 3**: [Competitor Name]
- Keywords they rank for that we don't: [List top 10]
- Opportunity: [Which to target first]

---

**CONTENT CLUSTERS TO BUILD**:

**Cluster 1: [Topic]** (Pillar page + supporting content)
- Pillar page: "[Comprehensive Guide to X]" (3,000+ words)
- Supporting post 1: "[Subtopic A]"
- Supporting post 2: "[Subtopic B]"
- Supporting post 3: "[Subtopic C]"
- Supporting post 4: "[Subtopic D]"
- Internal linking: All support posts link to pillar, pillar links to all supports

**Cluster 2: [Topic]**
[Repeat structure...]

**Cluster 3: [Topic]**
[Repeat structure...]

---

**KEYWORD DIFFICULTY & OPPORTUNITY**:

**Quick Wins** (Low competition, decent volume):
1. [Keyword] - Can rank in 1-3 months
2. [Keyword] - Can rank in 1-3 months
3. [Keyword] - Can rank in 1-3 months

**Medium-term Targets** (Medium competition):
1. [Keyword] - Can rank in 3-6 months
2. [Keyword] - Can rank in 3-6 months
3. [Keyword] - Can rank in 3-6 months

**Long-term Targets** (High competition, high reward):
1. [Keyword] - Can rank in 6-12 months
2. [Keyword] - Can rank in 6-12 months
3. [Keyword] - Can rank in 6-12 months

---

**SEARCH INTENT MAPPING**:

**Informational Intent** (Top of funnel):
- Keywords: "what is", "how to", "guide to", "benefits of"
- Content type: Blog posts, guides, educational videos
- Goal: Awareness, traffic

**Commercial Intent** (Middle of funnel):
- Keywords: "best", "top", "review", "comparison"
- Content type: Comparison pages, reviews, case studies
- Goal: Consideration, email capture

**Transactional Intent** (Bottom of funnel):
- Keywords: "buy", "price", "cost", "contractor", "near me"
- Content type: Product pages, pricing pages, contact forms
- Goal: Conversion, sales

---

**SEASONAL KEYWORD TRENDS**:

| Month | Trending Keywords | Search Volume Change | Strategy |
|-------|-------------------|---------------------|----------|
| Jan-Feb | [Keywords] | +__% | [Content to create] |
| Mar-Apr | [Keywords] | +__% | [Content to create] |
| May-Jun | [Keywords] | +__% | [Content to create] |
| Jul-Aug | [Keywords] | +__% | [Content to create] |
| Sep-Oct | [Keywords] | +__% | [Content to create] |
| Nov-Dec | [Keywords] | +__% | [Content to create] |

---

**CONTENT RECOMMENDATIONS**:

**Priority 1** (Create next):
1. [Page/post] targeting [keyword]
2. [Page/post] targeting [keyword]
3. [Page/post] targeting [keyword]

**Priority 2** (Create next month):
1. [Page/post] targeting [keyword]
2. [Page/post] targeting [keyword]

**Priority 3** (Create next quarter):
1. [Page/post] targeting [keyword]
2. [Page/post] targeting [keyword]

---

**TRACKING & MEASUREMENT**:

**KPIs to Track**:
- Keyword rankings (target top 3 positions)
- Organic traffic growth
- Click-through rate from SERPs
- Conversion rate from organic traffic
- Domain authority growth

**Tools**:
- Google Search Console (free)
- Google Analytics (free)
- Rank tracking tool (Ahrefs, SEMrush, or free alternatives)

**Monthly Reporting**:
- Top 10 ranking improvements
- Top 10 ranking declines (investigate why)
- New keywords entered top 100
- Traffic and conversion trends

Make data-driven decisions. Double down on what works."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def optimize_page(page_url, target_keyword):
    """
    Generate on-page SEO optimization recommendations.
    """
    
    prompt = f"""You are an SEO specialist optimizing {page_url} for keyword: {target_keyword}

**ON-PAGE SEO OPTIMIZATION CHECKLIST**

---

**TITLE TAG** (50-60 characters):

Current: [Assess if provided, otherwise suggest optimal]

✅ **Optimized Title**:
"[Target Keyword] | [Benefit/Value Prop] | [Brand Name]"

Example: "Micro-Hydro Power Systems | 60% Energy Cost Reduction | ResonanceEnergy"

**Best Practices**:
- Include target keyword near beginning
- Keep under 60 chars to avoid truncation
- Include brand name at end
- Make it click-worthy (use power words)

---

**META DESCRIPTION** (150-160 characters):

Current: [Assess if provided]

✅ **Optimized Description**:
"[Compelling hook with keyword]. [Key benefit]. [Call to action]. [Trust signal]."

Example: "Micro-hydro power systems that cut energy costs 60%. Proven ROI, 25-year lifespan, installed in 2 days. Get free site assessment today. 50+ installations nationwide."

**Best Practices**:
- Include target keyword naturally
- Highlight main benefit/value prop
- Include call to action
- Add trust signals (numbers, guarantees, social proof)
- Keep 150-160 chars

---

**URL STRUCTURE**:

Current: {page_url}

✅ **Optimized URL**:
[domain.com]/[category]/[target-keyword]/

Example: domain.com/solutions/micro-hydro-power-systems/

**Best Practices**:
- Include target keyword
- Keep short and readable
- Use hyphens (not underscores)
- Lowercase only
- Avoid special characters, parameters

---

**H1 HEADING** (One per page):

✅ **Optimized H1**:
"[Target Keyword]: [Benefit/Value Statement]"

Example: "Micro-Hydro Power Systems: Reliable Renewable Energy for Your Business"

**Best Practices**:
- Include target keyword
- Make it compelling (not just keyword stuffing)
- Only one H1 per page
- Different from title tag (avoid duplicate content)

---

**H2-H6 SUBHEADINGS** (Hierarchical structure):

Suggested heading structure:

**H2**: What is [Target Keyword]?
  - H3: How it works
  - H3: Key components

**H2**: Benefits of [Target Keyword]
  - H3: Cost savings
  - H3: Environmental impact
  - H3: Reliability

**H2**: [Target Keyword] Applications
  - H3: Commercial use
  - H3: Residential use
  - H3: Industrial use

**H2**: Pricing and ROI
  - H3: Cost breakdown
  - H3: Payback period

**H2**: Getting Started
  - H3: Site assessment
  - H3: Installation process

**Best Practices**:
- Use keyword variations in H2s
- Organize content logically
- Include related keywords in subheadings
- Make headings descriptive and scannable

---

**CONTENT OPTIMIZATION**:

**Target Word Count**: 1,500-3,000 words (longer for competitive keywords)

**Keyword Usage**:
- Primary keyword: Use 5-8 times naturally (0.5-1% density)
- First paragraph: Include keyword in first 100 words
- Variations: Use semantic variations and synonyms
- LSI keywords: Include related terms [list 10-15]

**Content Structure**:
1. **Introduction** (150-200 words):
   - Hook with problem/opportunity
   - Include target keyword
   - Promise value reader will get
   - Internal link to related content

2. **Body Content** (1,200-2,500 words):
   - Break into scannable sections (H2/H3)
   - Use short paragraphs (2-4 sentences)
   - Include bullet points and numbered lists
   - Add data, statistics, examples
   - Internal links to related pages (3-5)
   - External links to authoritative sources (2-3)

3. **Conclusion** (150-200 words):
   - Summarize key points
   - Reinforce main benefit
   - Strong call to action
   - Internal link to conversion page

**E-A-T Optimization** (Expertise, Authoritativeness, Trustworthiness):
- Author bio (credentials, expertise)
- Citations and references
- Customer testimonials
- Trust badges (certifications, awards)
- Contact information visible
- Last updated date

---

**IMAGE OPTIMIZATION**:

**Image 1** (Hero image):
- File name: target-keyword-hero-image.jpg
- Alt text: "[Descriptive text including target keyword]"
- Title: "[Brief description]"
- Size: Compress to <100KB
- Dimensions: Appropriate for responsive design

**Image 2-5** (Supporting images):
[Repeat for each image]

**Best Practices**:
- Descriptive file names (not IMG_1234.jpg)
- Alt text for accessibility and SEO
- Compress images (use tools like TinyPNG)
- Use next-gen formats (WebP)
- Lazy loading for below-fold images

---

**INTERNAL LINKING**:

**Links FROM this page TO**:
1. [Related topic page] - Anchor text: "[Natural anchor with keyword]"
2. [Related blog post] - Anchor text: "[Natural anchor]"
3. [Product/service page] - Anchor text: "[Action-oriented anchor]"
4. [Case study] - Anchor text: "[Benefit-focused anchor]"
5. [Contact page] - Anchor text: "[CTA anchor]"

**Links TO this page FROM**:
1. [Homepage] - Anchor text: "[Primary keyword]"
2. [Related service pages] - Anchor text: "[Keyword variation]"
3. [Blog posts] - Anchor text: "[Natural contextual anchor]"

**Best Practices**:
- Use descriptive anchor text (not "click here")
- Link to relevant, related content
- Don't over-optimize (vary anchor text)
- Aim for 3-5 internal links per 1,000 words
- Link deep (not just to homepage)

---

**EXTERNAL LINKING**:

**Outbound Links** (2-3 per page):
1. [Authoritative source] - Link to industry research/data
2. [Government/educational site] - Link to standards/regulations
3. [Industry organization] - Link to relevant resources

**Best Practices**:
- Link to high-authority sites (.gov, .edu, industry leaders)
- Use rel="noopener" for security
- Open in new tab (for external links)
- Relevant to your content

---

**SCHEMA MARKUP** (Structured data):

**Recommended Schema Types**:

1. **Organization Schema**:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "Customer Service"
  }
}
```

2. **Product Schema** (if product page):
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "image": "[Image URL]",
  "description": "[Description]",
  "brand": "[Brand]",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "[Price]"
  }
}
```

3. **FAQ Schema** (if FAQ section):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer]"
      }
    }
  ]
}
```

---

**PAGE SPEED OPTIMIZATION**:

**Critical Actions**:
- ✅ Compress images (<100KB each)
- ✅ Minify CSS and JavaScript
- ✅ Enable browser caching
- ✅ Use CDN for static assets
- ✅ Lazy load images below fold
- ✅ Remove unused CSS/JS
- ✅ Enable Gzip compression
- ✅ Optimize server response time (<200ms)

**Target Metrics**:
- Core Web Vitals: Pass all
- PageSpeed Insights: 90+ (mobile and desktop)
- Load time: <3 seconds

---

**MOBILE OPTIMIZATION**:

**Checklist**:
- ✅ Responsive design (mobile-first)
- ✅ Readable font sizes (16px minimum)
- ✅ Touch-friendly buttons (48px minimum)
- ✅ No horizontal scrolling
- ✅ Fast load time on 3G/4G
- ✅ Google Mobile-Friendly Test: Pass

---

**USER EXPERIENCE (UX) SIGNALS**:

**Improve Engagement**:
- Clear, scannable content
- Visual hierarchy (headings, whitespace)
- Multimedia (images, videos, infographics)
- Related content suggestions
- Easy navigation
- Fast load time
- Clear CTAs

**Target Metrics**:
- Time on page: 2+ minutes
- Bounce rate: <50%
- Pages per session: 2+

---

**CALL TO ACTION (CTA)**:

**Primary CTA** (Above fold):
"[Action-oriented text]"
Example: "Get Your Free Site Assessment"

**Secondary CTA** (Mid-page):
"[Alternative action]"
Example: "Download Our ROI Calculator"

**Final CTA** (Bottom of page):
"[Strong closing CTA]"
Example: "Start Saving on Energy Costs Today"

**Best Practices**:
- Action-oriented language
- Benefit-focused (not feature-focused)
- Contrasting color (stands out)
- Multiple CTAs per page (different options)
- Track conversion rates

---

**SOCIAL PROOF**:

**Include**:
- Customer testimonials (3-5 with photos)
- Trust badges (certifications, awards)
- Social proof numbers ("500+ installations")
- Client logos (if B2B)
- Star ratings (if applicable)
- Case study links

---

**TECHNICAL SEO CHECKS**:

- ✅ Page indexed (not blocked by robots.txt)
- ✅ Canonical tag (avoid duplicate content)
- ✅ No broken links (internal or external)
- ✅ HTTPS (SSL certificate)
- ✅ XML sitemap includes page
- ✅ Breadcrumb navigation
- ✅ Clean HTML (no errors)

---

**CONTENT FRESHNESS**:

**Update Plan**:
- Review quarterly for accuracy
- Add new data/statistics annually
- Update images/screenshots as needed
- Add "Last Updated: [Date]" at top
- Refresh meta description periodically
- Monitor rankings and update if declining

---

**COMPETITIVE ANALYSIS**:

**Top 3 Ranking Pages** for {target_keyword}:

**Competitor 1**: [URL]
- What they do well: [Analysis]
- What we can do better: [Opportunity]

**Competitor 2**: [URL]
- What they do well: [Analysis]
- What we can do better: [Opportunity]

**Competitor 3**: [URL]
- What they do well: [Analysis]
- What we can do better: [Opportunity]

**Our Competitive Advantage**:
[How to differentiate and outrank]

---

**OPTIMIZATION PRIORITY**:

**High Priority** (Fix now):
1. [Issue #1]
2. [Issue #2]
3. [Issue #3]

**Medium Priority** (Fix this month):
1. [Issue #4]
2. [Issue #5]

**Low Priority** (Nice to have):
1. [Enhancement #1]
2. [Enhancement #2]

---

**EXPECTED RESULTS**:

**Timeline**:
- Weeks 1-4: Indexing, initial ranking movement
- Months 2-3: Steady ranking improvements
- Months 4-6: Target page 1 ranking (position 1-10)
- Months 6-12: Maintain and improve to top 3

**Traffic Projection**:
- Current organic traffic: [X] visits/month
- 3-month projection: [X + Y] visits/month (+__%)
- 6-month projection: [X + Z] visits/month (+__%)

Implement these optimizations systematically and track results weekly."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def technical_seo_audit():
    """
    Comprehensive technical SEO audit checklist.
    """
    
    prompt = """You are conducting a comprehensive technical SEO audit.

**TECHNICAL SEO AUDIT CHECKLIST**

---

**1. CRAWLABILITY & INDEXABILITY**

**Robots.txt**:
- ✅ File exists at domain.com/robots.txt
- ✅ Allows important pages to be crawled
- ✅ Blocks admin, private, duplicate content pages
- ✅ Links to XML sitemap
- ⚠️ Check: No accidental blocking of important content

**XML Sitemap**:
- ✅ Exists at domain.com/sitemap.xml
- ✅ Submitted to Google Search Console
- ✅ Submitted to Bing Webmaster Tools
- ✅ Contains all important pages
- ✅ No 404 or redirect URLs
- ✅ Updated automatically when content changes
- ✅ Under 50,000 URLs (split if larger)
- ✅ Proper priority and changefreq values

**Index Status**:
- Check: site:[yourdomain.com] in Google
- Total indexed pages: [Number]
- Expected pages: [Number]
- Gap analysis: [Investigate missing pages]

**Indexing Directives**:
- ✅ Important pages: No noindex tags
- ✅ Duplicate content: Use canonical tags
- ✅ Low-value pages: Add noindex if appropriate

---

**2. SITE STRUCTURE & NAVIGATION**

**URL Structure**:
- ✅ Clean, readable URLs (not parameter-heavy)
- ✅ Consistent structure across site
- ✅ Hyphens (not underscores) in URLs
- ✅ Lowercase URLs
- ✅ Short URLs (<100 characters preferred)
- ⚠️ Avoid: Session IDs, unnecessary parameters

**Site Hierarchy**:
- ✅ Flat architecture (3 clicks from homepage to any page)
- ✅ Logical category structure
- ✅ Clear parent-child relationships
- ✅ Breadcrumb navigation on all pages

**Internal Linking**:
- ✅ Every page accessible from another
- ✅ Descriptive anchor text
- ✅ No orphan pages (pages with no internal links)
- ✅ Homepage has 50-100 internal links
- ✅ Important pages have more internal links

---

**3. PAGE SPEED & PERFORMANCE**

**Core Web Vitals** (Google's ranking factors):
- **LCP** (Largest Contentful Paint): <2.5 seconds ✅
- **FID** (First Input Delay): <100ms ✅
- **CLS** (Cumulative Layout Shift): <0.1 ✅

**PageSpeed Insights Scores**:
- Mobile: __/100 (target: 90+)
- Desktop: __/100 (target: 95+)

**Performance Optimizations**:
- ✅ Image compression (<100KB per image)
- ✅ Next-gen image formats (WebP)
- ✅ Lazy loading for below-fold images
- ✅ Minify CSS, JavaScript, HTML
- ✅ Remove unused code
- ✅ Browser caching enabled
- ✅ Gzip/Brotli compression enabled
- ✅ CDN for static assets
- ✅ Server response time <200ms
- ✅ Reduce redirects (each adds delay)
- ✅ Async loading for JavaScript
- ✅ Critical CSS inline, defer non-critical

---

**4. MOBILE OPTIMIZATION**

**Mobile-Friendly Test**:
- ✅ Passes Google Mobile-Friendly Test
- ✅ Responsive design (not separate mobile site)
- ✅ Text readable without zooming (16px minimum)
- ✅ Touch elements spaced appropriately (48px minimum)
- ✅ No horizontal scrolling
- ✅ Viewport meta tag configured
- ✅ Fast mobile load time

**Mobile Usability Issues**:
- Check Google Search Console > Mobile Usability
- Fix all reported issues

---

**5. HTTPS & SECURITY**

**SSL Certificate**:
- ✅ HTTPS enabled (not HTTP)
- ✅ Valid SSL certificate (not expired)
- ✅ All resources load over HTTPS (no mixed content)
- ✅ HTTP redirects to HTTPS (301 permanent)
- ✅ HSTS header implemented

**Security Headers**:
- ✅ Content-Security-Policy
- ✅ X-Frame-Options
- ✅ X-Content-Type-Options
- ✅ Referrer-Policy

---

**6. DUPLICATE CONTENT**

**Canonical Tags**:
- ✅ Every page has canonical tag
- ✅ Self-referential canonicals on originals
- ✅ Cross-domain canonicals where appropriate
- ✅ Consistent URL versions (www vs. non-www, trailing slash)

**URL Parameters**:
- ✅ Set parameter handling in Google Search Console
- ✅ Use canonical tags for filtered/sorted pages

**Duplicate Content Checks**:
- Site: operator search for duplicate titles
- Check for scraped/syndicated content
- Paginated content handled properly

---

**7. STRUCTURED DATA (SCHEMA)**

**Implemented Schema Types**:
- ✅ Organization schema (homepage)
- ✅ Product schema (product pages)
- ✅ Article schema (blog posts)
- ✅ FAQ schema (FAQ pages)
- ✅ BreadcrumbList schema (all pages)
- ✅ Local Business schema (if local business)
- ✅ Review schema (if applicable)

**Validation**:
- Test with Google Rich Results Test
- Check Google Search Console > Enhancements
- Fix all errors and warnings

---

**8. ON-PAGE ELEMENTS**

**Title Tags**:
- ✅ Every page has unique title
- ✅ 50-60 characters length
- ✅ Includes target keyword
- ✅ No duplicate titles

**Meta Descriptions**:
- ✅ Every page has unique description
- ✅ 150-160 characters length
- ✅ Includes target keyword
- ✅ Compelling, click-worthy

**Heading Tags**:
- ✅ One H1 per page
- ✅ Hierarchical structure (H1 > H2 > H3)
- ✅ Include keywords in headings

**Image Alt Tags**:
- ✅ All images have alt text
- ✅ Descriptive and include keywords
- ✅ Not keyword-stuffed

---

**9. INTERNATIONAL SEO** (if applicable)

**Hreflang Tags**:
- ✅ Implemented for multi-language sites
- ✅ Correct language codes (en-us, fr-fr, etc.)
- ✅ Self-referential and reciprocal
- ✅ X-default for fallback

**Country Targeting**:
- Set in Google Search Console
- Use country-specific domains if targeting specific countries

---

**10. LOCAL SEO** (if applicable)

**Google Business Profile**:
- ✅ Claimed and verified
- ✅ Complete and accurate information
- ✅ Regular posts and updates
- ✅ Respond to reviews
- ✅ Photos uploaded

**NAP Consistency**:
- ✅ Name, Address, Phone consistent across all citations
- ✅ Schema markup includes NAP
- ✅ Contact page has NAP

**Local Citations**:
- Listed on relevant directories
- Consistent information everywhere

---

**11. ERROR CHECKING**

**404 Errors**:
- Check Google Search Console > Coverage
- Fix or redirect broken pages
- Create custom 404 page with helpful links

**Redirect Chains**:
- Audit all redirects
- Fix redirect chains (A→B→C should be A→C)
- Remove unnecessary redirects

**Server Errors** (5xx):
- Monitor uptime
- Fix server configuration issues

**Soft 404s**:
- Pages returning 200 but showing "not found"
- Should return proper 404 status code

---

**12. BACKLINK PROFILE**

**Analyze Backlinks**:
- Total backlinks: [Number]
- Referring domains: [Number]
- Domain authority: [Score]

**Toxic Links**:
- Identify spammy or low-quality links
- Disavow if necessary

**Link Building Opportunities**:
- Competitor backlink gaps
- Broken link building
- Resource page links
- Industry directory submissions

---

**13. CONTENT QUALITY**

**Thin Content**:
- Identify pages with <300 words
- Expand, consolidate, or noindex

**Duplicate Content**:
- Use tools to find internal duplicates
- Rewrite or canonical

**Content Gaps**:
- Keyword research for missing topics
- Create comprehensive content

---

**14. USER EXPERIENCE**

**Navigation**:
- ✅ Clear, intuitive menu
- ✅ Search functionality
- ✅ Footer links

**Design**:
- ✅ Modern, professional design
- ✅ Consistent branding
- ✅ Good contrast and readability

**Engagement Metrics**:
- Time on site: Target 2+ minutes
- Bounce rate: Target <50%
- Pages per session: Target 2+

---

**15. ANALYTICS & TRACKING**

**Google Analytics**:
- ✅ Properly installed
- ✅ Goals configured
- ✅ Enhanced eCommerce (if eCommerce)
- ✅ Event tracking

**Google Search Console**:
- ✅ Property verified
- ✅ Sitemap submitted
- ✅ Regular monitoring of issues

**Conversion Tracking**:
- ✅ Forms, calls, purchases tracked
- ✅ Attribution models configured

---

**AUDIT SUMMARY**

**Critical Issues** (Fix immediately):
1. [Issue with high impact]
2. [Issue with high impact]
3. [Issue with high impact]

**Major Issues** (Fix this month):
1. [Important issue]
2. [Important issue]

**Minor Issues** (Fix this quarter):
1. [Lower priority issue]
2. [Lower priority issue]

**Opportunities**:
1. [Growth opportunity]
2. [Growth opportunity]

---

**ONGOING MAINTENANCE**

**Weekly**:
- Check Google Search Console for new issues
- Monitor rankings for target keywords
- Review analytics for traffic changes

**Monthly**:
- Full technical SEO check
- Content audit (update old content)
- Backlink profile review
- Competitor analysis

**Quarterly**:
- Comprehensive site audit
- Keyword research update
- Content strategy review
- Technical infrastructure review

Technical SEO is the foundation. Get this right before focusing on content and links."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def ranking_strategy(target_keywords):
    """
    Generate 90-day ranking strategy for target keywords.
    """
    
    prompt = f"""You are creating a 90-day SEO strategy to rank for: {target_keywords}

**90-DAY RANKING STRATEGY**

---

**GOAL**: Achieve page 1 rankings (position 1-10) for primary keywords

**Target Keywords**: {target_keywords}

---

**MONTH 1: FOUNDATION & OPTIMIZATION**

**Week 1-2: Technical SEO & On-Page**
- [ ] Complete technical SEO audit
- [ ] Fix all critical issues (404s, redirects, speed)
- [ ] Optimize title tags, meta descriptions, headings
- [ ] Implement schema markup
- [ ] Improve internal linking structure
- [ ] Ensure mobile-friendliness
- [ ] Submit/update sitemap

**Week 3-4: Content Development**
- [ ] Create/optimize pillar page (3,000+ words) targeting primary keyword
- [ ] Create 4 supporting blog posts (1,500+ words each)
- [ ] Keyword research for content cluster
- [ ] Competitive content analysis
- [ ] Content calendar for Month 2-3

**Deliverables**:
- Technical SEO audit report
- Optimized pages: [Number]
- New content pieces: 5
- Internal links added: 50+

**Expected Results**:
- Keywords entered top 100: 50% of targets
- Organic traffic: +10-15%

---

**MONTH 2: CONTENT & AUTHORITY BUILDING**

**Week 5-6: Content Expansion**
- [ ] Publish 6 new blog posts (1,500+ words each)
- [ ] Update/expand 3 existing pages
- [ ] Create FAQ page with schema
- [ ] Develop comparison pages (vs competitors)
- [ ] Create downloadable resources (PDFs, guides)

**Week 7-8: Link Building**
- [ ] Reach out to 50 relevant websites for backlinks
- [ ] Guest post on 2-3 industry blogs
- [ ] Broken link building (20 opportunities)
- [ ] Resource page links (10 opportunities)
- [ ] Industry directory submissions (10)
- [ ] HARO responses (10)

**Deliverables**:
- New content pieces: 6
- Updated pages: 3
- Backlinks acquired: 10-15
- Referring domains: +5-10

**Expected Results**:
- Keywords in top 100: 70% of targets
- Keywords in top 50: 30% of targets
- Organic traffic: +25-35% (cumulative)

---

**MONTH 3: SCALE & OPTIMIZATION**

**Week 9-10: Content Velocity**
- [ ] Publish 8 new blog posts
- [ ] Create long-form content (5,000+ word guide)
- [ ] Video content (3-5 videos)
- [ ] Infographic creation
- [ ] Case studies (2)

**Week 11-12: Link Building Acceleration**
- [ ] Reach out to 100 relevant websites
- [ ] Guest posts: 3-5
- [ ] Digital PR campaign (press release)
- [ ] Influencer outreach (10 influencers)
- [ ] Link reclamation (unlinked brand mentions)
- [ ] Competitor backlink replication (20 links)

**Conversion Optimization**:
- [ ] A/B test CTAs
- [ ] Improve conversion paths
- [ ] Add social proof
- [ ] Optimize forms

**Deliverables**:
- New content pieces: 10+
- Backlinks acquired: 20-30
- Video content: 3-5
- Case studies: 2

**Expected Results**:
- Keywords in top 50: 50% of targets
- Keywords in top 20: 30% of targets
- Keywords on page 1 (1-10): 20% of targets
- Organic traffic: +50-75% (cumulative)

---

**CONTENT STRATEGY BY KEYWORD INTENT**

**Informational Keywords**:
- Content type: Blog posts, guides, how-tos
- Example: "How does micro-hydro work?"
- Create: 15-20 blog posts

**Commercial Keywords**:
- Content type: Comparison pages, reviews, best-of lists
- Example: "Best micro-hydro systems for businesses"
- Create: 5-7 comparison pages

**Transactional Keywords**:
- Content type: Product/service pages, pricing pages
- Example: "Buy micro-hydro system"
- Create/optimize: 3-5 conversion pages

---

**LINK BUILDING TARGETS BY MONTH**

**Month 1**:
- Low-hanging fruit (easy wins)
- Internal link optimization
- Business directories
- Industry associations
- Target: 5-10 backlinks

**Month 2**:
- Guest posting
- Resource pages
- Broken link building
- HARO
- Target: 10-15 backlinks

**Month 3**:
- Digital PR
- Influencer outreach
- Competitor backlink replication
- High-authority targets
- Target: 20-30 backlinks

**90-Day Total**: 35-55 new backlinks from relevant, high-quality sources

---

**CONTENT PUBLISHING CALENDAR**

**Total Content to Create**:
- Pillar pages: 1-2 (3,000+ words)
- Blog posts: 20+ (1,500+ words)
- Long-form guides: 2-3 (5,000+ words)
- Case studies: 2-3
- Videos: 3-5
- Infographics: 2-3
- FAQs: 1 comprehensive page

**Publishing Frequency**:
- Week 1-4: 2 posts/week
- Week 5-8: 2-3 posts/week
- Week 9-12: 3-4 posts/week

---

**TECHNICAL IMPROVEMENTS TIMELINE**

**Week 1**:
- Site speed optimization
- Mobile optimization
- HTTPS implementation (if needed)

**Week 4**:
- Schema markup addition
- Internal linking enhancement
- URL structure optimization

**Week 8**:
- Content refresh (update old posts)
- 404 error fixes
- Redirect cleanup

**Week 12**:
- Advanced technical optimizations
- Progressive Web App features
- Advanced schema types

---

**COMPETITOR OUTRANKING STRATEGY**

**For Each Target Keyword**:

1. **Analyze Top 3 Ranking Pages**:
   - Content length
   - Content quality
   - Backlink profile
   - Domain authority

2. **Create 10x Better Content**:
   - Longer (25-50% more content)
   - More comprehensive
   - Better formatted
   - Better visuals
   - More recent data

3. **Match/Exceed Backlinks**:
   - Identify their backlinks
   - Replicate those links
   - Find additional opportunities

4. **Optimize Better**:
   - Better title tags
   - Better meta descriptions
   - Better on-page optimization

---

**TRACKING & METRICS**

**Weekly Tracking**:
- Keyword rankings (track all target keywords)
- Organic traffic
- New backlinks
- Top-performing content

**Monthly Reporting**:
| Metric | Baseline | Month 1 | Month 2 | Month 3 | Target |
|--------|----------|---------|---------|---------|--------|
| Keywords top 100 | __% | __% | __% | __% | 100% |
| Keywords top 50 | __% | __% | __% | __% | 70% |
| Keywords top 20 | __% | __% | __% | __% | 40% |
| Keywords page 1 | __% | __% | __% | __% | 20% |
| Organic traffic | __ | __ | __ | __ | +75% |
| Backlinks | __ | __ | __ | __ | +50 |
| Referring domains | __ | __ | __ | __ | +20 |

---

**BUDGET ALLOCATION** (90 days):

- Content creation (writers, editors): $___
- Link building (outreach, guest posts): $___
- Technical SEO (developer time): $___
- Tools (Ahrefs, SEMrush, etc.): $___
- Design (graphics, infographics): $___
- PR/outreach: $___
- **Total**: $___

---

**RISK MITIGATION**:

**Potential Issues**:
1. **Algorithm updates**: Diversify strategy, focus on quality
2. **Slow ranking progress**: Patience, consistency, more content
3. **Competitor aggression**: Accelerate content and link building
4. **Technical issues**: Regular audits, quick fixes

**Contingency Plans**:
- If not ranking by Month 2, analyze and pivot
- If penalties, immediate cleanup and recovery
- If budget constraints, prioritize highest-impact activities

---

**SUCCESS FACTORS**:

1. **Consistency**: Publish content regularly
2. **Quality over quantity**: Better content > more content
3. **Relevance**: Target right keywords with right intent
4. **Authority**: Build quality backlinks
5. **Technical excellence**: Fast, mobile-friendly, error-free site
6. **User experience**: Engage visitors, reduce bounce rate
7. **Patience**: SEO takes time (3-6 months minimum)

---

**AFTER 90 DAYS**:

**Expected Outcomes**:
- 50-75% increase in organic traffic
- 20%+ of target keywords ranking on page 1
- 40%+ of target keywords ranking in top 20
- 70%+ of target keywords ranking in top 50
- Domain authority increase of 5-10 points
- 35-55 new quality backlinks

**Next Steps**:
- Scale successful strategies
- Target more competitive keywords
- Expand content topics
- Build more high-authority links
- Optimize for conversions

SEO is a marathon, not a sprint. Stay consistent, measure results, and continuously improve."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ SEO Specialist initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python seo_specialist.py <command> [parameters]")
        print("\nCommands:")
        print("  keywords <topic>           - Keyword research for topic")
        print("  optimize <url> <keyword>   - On-page optimization recommendations")
        print("  audit                      - Technical SEO audit checklist")
        print("  strategy <keywords>        - 90-day ranking strategy")
        print("\nExamples:")
        print("  python seo_specialist.py keywords 'micro-hydro power'")
        print("  python seo_specialist.py optimize '/solutions' 'micro-hydro systems'")
        print("  python seo_specialist.py audit")
        print("  python seo_specialist.py strategy 'micro-hydro, hydropower systems'")
    else:
        command = sys.argv[1].lower()
        
        if command == 'keywords':
            topic = sys.argv[2] if len(sys.argv) > 2 else 'renewable energy'
            print(f"🔍 Researching keywords for: {topic}...\n")
            result = keyword_research(topic)
            print(result)
            
        elif command == 'optimize':
            url = sys.argv[2] if len(sys.argv) > 2 else '/page'
            keyword = sys.argv[3] if len(sys.argv) > 3 else 'target keyword'
            print(f"🎯 Optimizing {url} for '{keyword}'...\n")
            result = optimize_page(url, keyword)
            print(result)
            
        elif command == 'audit':
            print("📋 Running technical SEO audit...\n")
            result = technical_seo_audit()
            print(result)
            
        elif command == 'strategy':
            keywords = sys.argv[2] if len(sys.argv) > 2 else 'target keywords'
            print(f"📈 Creating 90-day ranking strategy for: {keywords}...\n")
            result = ranking_strategy(keywords)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: keywords, optimize, audit, strategy")
