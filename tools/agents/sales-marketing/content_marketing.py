"""
CONTENT MARKETING AGENT
Creates blog posts, case studies, whitepapers, and content strategies.
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

def write_blog_post(topic, length=1500):
    """
    Write SEO-optimized blog post on given topic.
    """
    
    prompt = f"""You are an expert content marketer for a micro-hydro renewable energy company. Write a comprehensive blog post on: {topic}

Target length: {length} words

**BLOG POST STRUCTURE**:

**Title**: [Compelling, SEO-friendly title with power words]
- Make it click-worthy but honest
- Include primary keyword
- 50-60 characters ideal

**Meta Description** (150-160 chars):
[Summary that entices clicks from search results]

**Hook** (First 100 words):
Start with a compelling statistic, question, or story that hooks readers immediately. Make them want to keep reading.

**Introduction** (200 words):
- Problem statement (what challenge does reader face?)
- Why it matters (consequences of inaction)
- What this post covers (roadmap)
- Promise value (what reader will learn)

**Main Content** (Break into 3-5 H2 sections with H3 subsections):

Use this structure:
- **H2: [Main Point 1]**
  - H3: [Subpoint]
  - H3: [Subpoint]
  - Include: Data, examples, quotes, visuals descriptions
  
- **H2: [Main Point 2]**
  - H3: [Subpoint]
  - H3: [Subpoint]
  - Include: Case study, real-world application
  
- **H2: [Main Point 3]**
  - H3: [Subpoint]
  - H3: [Subpoint]
  - Include: Actionable advice, frameworks

**Content Elements to Include**:
- Statistics and data (cite sources)
- Real examples from micro-hydro industry
- Quotes from experts or customers
- Bullet points for scannability
- Bold key takeaways
- Internal links (suggest 3-5 related topics)
- External links to authoritative sources

**Conclusion** (150 words):
- Recap main points
- Reinforce key takeaway
- Call to action (what reader should do next)

**Call to Action**:
[Specific next step - download resource, schedule consultation, read related post]

**SEO Optimization**:
- Primary keyword: [Identify and use 3-5 times naturally]
- Secondary keywords: [List 3-5 related terms]
- Internal links: [Suggest 3-5 related posts to link to]
- External links: [Suggest 2-3 authoritative sources]
- Image suggestions: [Describe 3-5 images/graphics to include]

**Tone**: Professional but accessible, educational but engaging, technical but not jargon-heavy

**Goal**: Establish thought leadership, drive organic traffic, generate leads

Write the complete blog post now:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def create_case_study(customer_name, results):
    """
    Write customer success case study.
    """
    
    prompt = f"""You are writing a compelling case study for {customer_name} who achieved: {results}

**CASE STUDY STRUCTURE**:

**Title**: [Customer Name] Achieved [Quantified Result] with [Your Solution]
Example: "Rural Hotel Cuts Energy Costs 60% with Micro-Hydro Installation"

**Executive Summary** (100 words):
One paragraph that captures:
- Who the customer is
- What problem they faced
- What solution you provided
- What results they achieved

**At a Glance Box**:
| | |
|---|---|
| **Industry** | [Industry] |
| **Location** | [Location] |
| **Challenge** | [One sentence] |
| **Solution** | [One sentence] |
| **Results** | [Bulleted list of top 3-5 metrics] |
| **Timeframe** | [How long to implement and achieve results] |

---

**The Challenge** (200-300 words)

Start with customer's voice:
> "Quote from customer describing their problem"

Describe the situation:
- What was happening before your solution
- Why it was a problem (costs, inefficiency, etc.)
- What they tried before (why alternatives didn't work)
- Why they chose your company

Include specifics:
- Quantified problems ($X wasted, Y hours lost, Z% inefficiency)
- Timeline context (how long problem existed)
- Urgency factors (regulatory, competitive, financial pressures)

---

**The Solution** (300-400 words)

Describe what you implemented:

**Discovery & Planning**:
- Initial consultation and site assessment
- Custom design based on their needs
- Timeline and budget agreed upon

**Implementation**:
- What equipment/system was installed
- Technical specifications (appropriate level of detail)
- Project timeline (start to finish)
- Team involved (your company + customer)

**Key Differentiators**:
- What made your approach unique
- How you overcame challenges
- Why customer chose you over alternatives

Include customer quote:
> "Quote about working with your team / implementation process"

**Visual Descriptions**:
- [Describe before photo]
- [Describe installation process photo]
- [Describe after photo]

---

**The Results** (300-400 words)

Lead with strongest metrics:

**Quantified Outcomes**:
- 💰 **Cost Savings**: Reduced energy costs by __% = $__k annually
- ⚡ **Energy Production**: Generating __kW, powering __% of facility
- 🌱 **Environmental Impact**: Avoiding __ tons CO2 annually
- 📈 **ROI**: Payback period of __ years, __% annual return
- 🏆 **Other Benefits**: [Reliability, energy independence, brand value]

**Before vs. After Comparison**:
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Monthly energy cost | $__ | $__ | -__% |
| Energy from renewables | __% | __% | +__% |
| Carbon footprint | __ tons | __ tons | -__% |
| Grid outages impact | __ hrs lost | __ hrs lost | -__% |

**Customer Testimonial**:
> "Extended quote from customer about results, experience, and recommendation"

**Unexpected Benefits**:
- [Things customer didn't anticipate but got anyway]
- Marketing/PR value of renewable energy
- Employee morale, customer perception, etc.

---

**Looking Ahead** (100-150 words)

- What's next for this customer
- Expansion plans or additional projects
- Long-term relationship value

Final customer quote:
> "Quote about future plans or why they'd recommend you"

---

**Call to Action**:
"Achieve similar results for your [facility/business]."
[Contact button / Download full case study PDF / Schedule consultation]

---

**Sidebar - Company Profile**:
**About {customer_name}**:
- Industry
- Size/employees
- Location
- What they do
- Website

---

**SEO Elements**:
- Title tag (60 chars): [SEO-optimized title]
- Meta description (155 chars): [Compelling summary]
- Keywords: [List 5-7 relevant keywords]
- Alt text for images: [Describe for each image]

**Promotion Strategy**:
- Share on LinkedIn (customer tags your company)
- Feature in email newsletter
- Present at industry conferences
- Use in sales proposals
- Include in media kit

**Success Metrics to Track**:
- Views/downloads
- Leads generated
- Sales influenced
- Social shares

Make this case study so compelling that prospects think "I want those results too" and reach out."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def content_calendar(duration='month'):
    """
    Generate content calendar for blog, social, email.
    
    Duration: week, month, quarter, year
    """
    
    prompt = f"""You are a content strategist creating a comprehensive {duration} content calendar for a micro-hydro renewable energy company.

**CONTENT MARKETING CALENDAR - {duration.upper()}**

---

**STRATEGIC THEMES** (for the {duration}):

Theme 1: [E.g., "Cost Savings & ROI"]
- Goal: Drive commercial/industrial leads
- Target audience: CFOs, facility managers
- Key messages: Energy cost reduction, fast payback, long-term value

Theme 2: [E.g., "Sustainability & ESG"]
- Goal: Appeal to environmentally-conscious companies
- Target audience: Sustainability directors, corporate leadership
- Key messages: Carbon reduction, renewable energy goals, corporate responsibility

Theme 3: [E.g., "Technology & Innovation"]
- Goal: Establish thought leadership
- Target audience: Engineers, technical decision-makers
- Key messages: Cutting-edge design, efficiency, reliability

Theme 4: [E.g., "Community & Impact"]
- Goal: Build brand awareness and goodwill
- Target audience: General public, media, advocates
- Key messages: Rural development, energy independence, local benefits

---

**BLOG POSTS** (2-4 per week):

**Week 1**:
- Monday: "[Title]" (Theme: [X], Length: [Y] words, Author: [Who], Keywords: [List])
  - Target: [Audience]
  - CTA: [What action]
  - Internal links: [Related posts]
  
- Wednesday: "[Title]" (Theme: [X], Length: [Y] words, Author: [Who], Keywords: [List])
  - Target: [Audience]
  - CTA: [What action]
  
- Friday: "[Title]" (Theme: [X], Length: [Y] words, Author: [Who], Keywords: [List])
  - Target: [Audience]
  - CTA: [What action]

**Week 2**:
[Continue pattern...]

**Week 3**:
[Continue pattern...]

**Week 4**:
[Continue pattern...]

---

**LONG-FORM CONTENT** (Monthly):

**Week 1-2**: Whitepaper
- Title: "[Comprehensive Guide to X]"
- Length: 3,000-5,000 words
- Research required: [Days]
- Design required: Yes (PDF layout)
- Lead magnet: Gated download
- Promotion: Email campaign + LinkedIn ads

**Week 3**: Case Study
- Customer: [Name/type]
- Results to highlight: [Metrics]
- Interview needed: Yes
- Photos needed: Yes
- Format: Web page + PDF
- Distribution: Sales team, website, social

**Week 4**: Webinar
- Topic: "[Topic]"
- Presenter: [Internal expert]
- Guest: [Industry expert or customer]
- Date/time: [Specific]
- Promotion: 2-week lead time
- Follow-up: Recording, slides, Q&A summary

---

**SOCIAL MEDIA POSTS**:

**LinkedIn** (Daily):
- Monday: Industry news commentary (Theme: [X])
  - Post type: Text + link
  - Hashtags: [List 3-5]
  - Goal: Engagement
  
- Tuesday: Employee spotlight or behind-the-scenes
  - Post type: Image + story
  - Goal: Humanize brand
  
- Wednesday: Blog post promotion
  - Post type: Link + excerpt
  - Goal: Drive traffic
  
- Thursday: Customer success highlight
  - Post type: Image + testimonial
  - Goal: Social proof
  
- Friday: Educational content (tips, how-to)
  - Post type: Carousel or video
  - Goal: Thought leadership

**Twitter** (2-3x daily):
- Morning: Industry news, trending topics
- Midday: Company updates, product info
- Evening: Engaging questions, polls

**Facebook** (3x weekly):
- Longer-form storytelling
- Community engagement
- Event promotion
- Customer spotlights

**Instagram** (3x weekly):
- Project photos (before/after)
- Team culture
- Environmental impact visuals

**YouTube** (Weekly):
- Project walkthroughs
- Customer testimonials (video)
- Educational explainers
- Webinar recordings

---

**EMAIL CAMPAIGNS**:

**Weekly Newsletter** (Every Tuesday):
- Lead story: Featured blog post or news
- Section 2: Customer spotlight
- Section 3: Industry news roundup
- Section 4: Resource (guide, tool, template)
- CTA: [Primary action]

**Monthly Deep Dive** (First Thursday):
- Focus: One theme in depth
- Content: Long-form article or whitepaper excerpt
- Exclusive offer: Early access to content, discount, consultation

**Nurture Sequences** (Automated):
- Lead magnet download → 6-email sequence
- Trial/demo signup → 5-email sequence
- Customer onboarding → 8-email sequence
- Re-engagement → 4-email sequence

---

**VIDEO CONTENT**:

**Week 1**: Explainer video
- Topic: "How Micro-Hydro Works in 60 Seconds"
- Length: :60
- Distribution: Website, social, ads

**Week 2**: Customer testimonial (video)
- Customer: [Name]
- Length: 2-3 minutes
- Questions: Challenge, solution, results
- Distribution: Website, sales materials, social

**Week 3**: Project showcase
- Location: [Project name]
- Length: 3-5 minutes
- Content: Site tour, system operation, benefits
- Distribution: YouTube, website, email

**Week 4**: Expert interview
- Guest: [Industry expert or internal engineer]
- Topic: [Relevant trend or technology]
- Length: 10-15 minutes (or podcast episode)
- Distribution: YouTube, LinkedIn, website

---

**PODCAST** (If applicable - Bi-weekly):
- Episode 1: "[Title]" - Guest: [Name], Topic: [X]
- Episode 2: "[Title]" - Guest: [Name], Topic: [X]

---

**CONTENT PRODUCTION SCHEDULE**:

**2 Weeks Before Publishing**:
- Topic research and outline
- Interviews scheduled (if needed)
- Source materials gathered

**1 Week Before Publishing**:
- First draft written
- Internal review
- Revisions

**3 Days Before Publishing**:
- Final edit
- SEO optimization
- Graphics/images created
- Social media snippets prepared

**Day of Publishing**:
- Publish to website
- Email blast sent
- Social media posts scheduled
- Team notified (for shares/engagement)

**1 Day After Publishing**:
- Monitor engagement
- Respond to comments
- Track metrics

---

**CONTENT REPURPOSING STRATEGY**:

Blog Post →
- LinkedIn article
- Twitter thread
- Email newsletter feature
- Social media graphics (pull quotes)
- Podcast episode discussion
- Webinar topic

Webinar →
- Blog post summary
- YouTube video
- Social media clips
- Email nurture content
- Sales presentation slides

Case Study →
- Blog post
- Social media series
- Email campaign
- Sales leave-behind
- Conference presentation

Whitepaper →
- Blog series (4-5 posts)
- Infographic
- Webinar
- LinkedIn article series
- Sales toolkit

---

**METRICS TO TRACK**:

**Content Performance**:
- Page views, unique visitors
- Time on page, bounce rate
- Social shares, comments
- Backlinks earned
- Keyword rankings

**Lead Generation**:
- Form submissions (gated content)
- Email signups
- Contact requests
- Demo/consultation bookings

**Engagement**:
- Email open rates, click rates
- Social engagement rates
- Video view completion rates
- Webinar attendance rates

**SEO**:
- Organic traffic growth
- Keyword ranking improvements
- Domain authority growth
- Featured snippets earned

**Sales Impact**:
- Content-influenced leads
- Content-influenced deals
- Sales team usage rates

---

**TEAM RESPONSIBILITIES**:

**Content Manager**: Overall strategy, calendar management, quality control
**Writer(s)**: Blog posts, case studies, scripts
**Designer**: Graphics, infographics, presentation slides
**Video Editor**: Video content, social media clips
**SEO Specialist**: Keyword research, optimization, technical SEO
**Social Media Manager**: Social posting, community engagement
**Subject Matter Experts**: Technical review, interviews, guest posts

---

**BUDGET ALLOCATION** (if {duration} = month):
- Freelance writers: $__
- Design/graphics: $__
- Video production: $__
- Photography: $__
- Tools/software: $__
- Promotion (ads): $__
- Total: $__

---

**CONTENT GOALS FOR {duration.upper()}**:
- Website traffic: Increase by __%
- Blog subscribers: Add __ new
- Social followers: Grow by __%
- Gated content downloads: __ downloads
- Leads generated: __ qualified leads
- Sales opportunities influenced: $__ pipeline

---

**COMPETITOR ANALYSIS**:
Monitor these competitors' content:
- [Competitor 1]: What they're doing well, what gaps exist
- [Competitor 2]: Content frequency, topics, engagement
- [Competitor 3]: Unique angles, differentiators

---

**CONTENT BEST PRACTICES**:
✅ Write for humans first, search engines second
✅ Use data and examples (not just theory)
✅ Include clear CTAs in every piece
✅ Optimize for mobile reading
✅ Build internal linking structure
✅ Update old content regularly
✅ Promote content multiple times (different angles)
✅ Engage with comments and shares
✅ A/B test headlines and CTAs
✅ Analyze what works, do more of it

This calendar is a living document. Adjust based on performance, trends, and business priorities."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def social_media_campaign(campaign_goal, duration='week'):
    """
    Generate social media campaign across all platforms.
    
    Goals: awareness, leads, engagement, traffic, sales
    """
    
    prompt = f"""You are a social media strategist. Create {duration}-long campaign to achieve: {campaign_goal}

**SOCIAL MEDIA CAMPAIGN BRIEF**

---

**Campaign Overview**:

**Goal**: {campaign_goal}
**Duration**: {duration}
**Target Audience**: [Define primary and secondary]
**Key Message**: [Central theme/value proposition]
**Success Metrics**: [Specific, measurable KPIs]

---

**CAMPAIGN STRATEGY**:

**Phase 1 - Awareness** (Days 1-2):
- Introduce campaign theme
- Tease valuable content/offer
- Build anticipation
- Broad targeting

**Phase 2 - Engagement** (Days 3-5):
- Share valuable content
- Encourage interaction (polls, questions, UGC)
- Build community conversation
- Respond to all comments

**Phase 3 - Conversion** (Days 6-7):
- Strong CTA to convert
- Time-limited offer/urgency
- Social proof (testimonials, results)
- Retarget engaged users

---

**CONTENT CALENDAR** (Daily breakdown):

**DAY 1** - Launch Day

**LinkedIn**:
- **Morning (9 AM)**: Campaign announcement post
  - Format: Text + image/video
  - Content: "[Hook] We're launching [campaign]. Here's why it matters: [value proposition]. [CTA to learn more] #hashtag"
  - Expected engagement: __ likes, __ comments, __ shares
  - Budget: $__ (boost post)

- **Afternoon (2 PM)**: Behind-the-scenes
  - Format: Carousel images
  - Content: "How we're preparing for [campaign]..."
  - Goal: Humanize brand

**Twitter**:
- **Morning (8 AM)**: Teaser tweet
  - Content: "🚨 Big announcement coming at 9 AM. It's about [topic]. Stay tuned..."
  
- **Morning (9 AM)**: Announcement tweet + thread
  - Tweet 1: Campaign intro
  - Tweet 2-5: Key benefits/features
  - Tweet 6: CTA
  - Include: Image, hashtag, link

- **Afternoon (3 PM)**: Poll
  - Question: "[Engaging question related to campaign]"
  - Options: A, B, C, D
  - Goal: Engagement, data collection

- **Evening (7 PM)**: User-focused tweet
  - Content: "You told us [pain point]. We listened. [Solution from campaign]"

**Facebook**:
- **Morning (10 AM)**: Campaign launch post
  - Format: Video (1-2 minutes)
  - Content: Explainer of campaign, benefits, CTA
  - Targeting: Saved audience + lookalikes
  - Budget: $__/day

**Instagram**:
- **Morning (8 AM)**: Story series (5-7 slides)
  - Slide 1: Teaser
  - Slide 2-4: Key points
  - Slide 5: Countdown
  - Slide 6: Link sticker to landing page
  - Slide 7: Poll/question sticker

- **Afternoon (12 PM)**: Feed post
  - Format: Carousel (4-6 images)
  - Content: Campaign visuals + copy
  - Hashtags: [List 20-30 relevant hashtags]

**YouTube**:
- **Morning (9 AM)**: Campaign video release
  - Title: "[Attention-grabbing title with keyword]"
  - Length: 3-5 minutes
  - Description: [Full description with links, timestamps, keywords]
  - End screen: CTA to landing page

---

**DAY 2** - Value Delivery

[Continue pattern for each day with specific posts, timings, formats, and goals]

---

**DAY 3** - Engagement Focus

[Continue...]

---

**DAY 4** - Social Proof

[Continue...]

---

**DAY 5** - Educational Content

[Continue...]

---

**DAY 6** - Urgency Build

[Continue...]

---

**DAY 7** - Final Push

[Continue...]

---

**CONTENT THEMES BY PLATFORM**:

**LinkedIn** (B2B focus):
- Industry insights and trends
- Case studies and ROI data
- Thought leadership
- Customer spotlights
- Technical content

**Twitter** (News and engagement):
- Quick tips and facts
- Industry news commentary
- Questions and polls
- Thread-based storytelling
- Real-time engagement

**Facebook** (Community building):
- Longer-form storytelling
- Community questions
- Events and webinars
- User-generated content
- Behind-the-scenes

**Instagram** (Visual storytelling):
- Project photos
- Before/after transformations
- Team culture
- Environmental impact visuals
- Stories for engagement

**YouTube** (Long-form education):
- How-to videos
- Customer testimonials
- Project walkthroughs
- Webinar recordings
- Educational series

---

**PAID PROMOTION STRATEGY**:

**Budget Allocation** ({duration}):
- LinkedIn ads: $__ (B2B lead gen)
- Facebook ads: $__ (Awareness + conversions)
- Instagram ads: $__ (Visual engagement)
- Twitter ads: $__ (Engagement, optional)
- YouTube ads: $__ (Pre-roll video)
- Total: $__

**Targeting**:
- Saved audiences: [Define]
- Lookalike audiences: Based on website visitors, email list
- Retargeting: Website visitors (last 30 days), engaged users
- Geographic: [Regions]
- Demographic: [Age, job title, industry, etc.]

**Ad Formats**:
- LinkedIn: Sponsored content, InMail
- Facebook: Single image, video, carousel, collection
- Instagram: Story ads, feed ads
- YouTube: Skippable video ads

---

**INFLUENCER/PARTNER OUTREACH**:

Reach out to:
1. **Industry Influencers** (3-5):
   - [Name], [followers], [niche]
   - Ask: Share campaign post, create content, guest blog
   - Offer: [Partnership, fee, or cross-promotion]

2. **Partner Companies** (5-10):
   - [Complementary businesses]
   - Ask: Cross-promote to their audiences
   - Offer: Reciprocal promotion

3. **Customers** (10-15):
   - Happy customers with social presence
   - Ask: Share their experience, testimonial
   - Offer: Incentive, feature in content

---

**USER-GENERATED CONTENT (UGC)**:

**Campaign Hashtag**: #[UniqueHashtag]

**UGC Contest** (Optional):
- Prompt: "Share your [X] and tag #[hashtag] for a chance to win [prize]"
- Prize: [Valuable offer]
- Selection criteria: Most creative, most likes, random draw
- Promotion: Share best entries, create showcase

---

**EMAIL INTEGRATION**:

Day 1: Email to subscribers announcing campaign
Day 3: Email to engaged segment with value content
Day 6: Email to all subscribers with urgency/FOMO
Day 8: Post-campaign thank you + results

---

**LANDING PAGE**:

**URL**: [Campaign-specific landing page]

**Elements**:
- Headline: [Compelling headline matching campaign message]
- Subhead: [Supporting detail]
- Hero image/video: [Visual that captures attention]
- Benefits section: [3-5 key benefits]
- Social proof: Testimonials, logos, stats
- CTA: [Clear action - download, register, buy, contact]
- Exit intent popup: Last chance offer

---

**COMMUNITY ENGAGEMENT PLAN**:

**Response Strategy**:
- Respond to all comments within 2 hours
- Like/heart all positive mentions
- Address questions and concerns promptly
- Thank users for shares and tags

**Engagement Tactics**:
- Ask questions in posts (encourage comments)
- Create polls (easy participation)
- Host live Q&A sessions (real-time engagement)
- Share and comment on user posts (build relationships)
- Join relevant conversations (thought leadership)

---

**METRICS & TRACKING**:

**Daily Tracking**:
- Impressions, reach
- Engagement rate (likes, comments, shares)
- Click-through rate (link clicks)
- Video views, completion rate
- Follower growth

**Campaign Tracking**:
- Landing page traffic (from social)
- Lead/conversion rate
- Cost per lead/acquisition
- ROI calculation
- Sentiment analysis

**Tools**:
- Native platform analytics
- Google Analytics (UTM tracking)
- Social media management tool (Hootsuite, Buffer, Sprout)
- CRM integration (track leads to sales)

---

**SUCCESS BENCHMARKS**:

**Awareness Campaign**:
- Reach: [X] impressions
- Engagement: [Y%] engagement rate
- Growth: [Z] new followers

**Lead Generation Campaign**:
- Traffic: [X] landing page visits
- Conversions: [Y] leads
- Cost: $[Z] cost per lead

**Sales Campaign**:
- Opportunities: [X] sales qualified leads
- Revenue: $[Y] attributed revenue
- ROI: [Z]x return on ad spend

---

**CONTINGENCY PLANS**:

**If engagement is low**:
- Increase ad spend on top-performing posts
- Try different content formats (video > image)
- Boost posts with highest organic engagement
- Re-target engaged users with stronger CTA

**If negative sentiment**:
- Address concerns transparently
- Pivot messaging if needed
- Increase customer testimonials/social proof
- Have PR/crisis communication plan ready

**If competitors respond**:
- Differentiate clearly
- Lean into unique value propositions
- Don't engage in negative campaigning
- Double down on customer success stories

---

**POST-CAMPAIGN**:

**Week After**:
- Results summary report
- Top-performing content analysis
- Audience insights captured
- Leads passed to sales
- Thank you content to participants

**Retargeting** (Ongoing):
- Retarget engaged users who didn't convert
- Nurture new followers with regular content
- Build custom audiences for future campaigns

**Learnings Documentation**:
- What worked (do more)
- What didn't (avoid or improve)
- Audience insights (inform future campaigns)
- Budget optimization (reallocate based on ROI)

---

This campaign should generate significant {campaign_goal} results while building long-term audience relationships."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Content Marketing initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python content_marketing.py <command> [parameters]")
        print("\nCommands:")
        print("  blog <topic> [length]           - Write blog post")
        print("  case_study <customer> <results> - Create case study")
        print("  calendar <duration>             - Generate content calendar (week/month/quarter/year)")
        print("  campaign <goal> <duration>      - Social media campaign (awareness/leads/engagement/traffic/sales)")
        print("\nExamples:")
        print("  python content_marketing.py blog 'ROI of Micro-Hydro' 2000")
        print("  python content_marketing.py case_study 'Mountain Resort' '60% cost reduction'")
        print("  python content_marketing.py calendar month")
        print("  python content_marketing.py campaign leads week")
    else:
        command = sys.argv[1].lower()
        
        if command == 'blog':
            topic = sys.argv[2] if len(sys.argv) > 2 else 'Benefits of Micro-Hydro Power'
            length = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
            print(f"✍️ Writing blog post: {topic} ({length} words)...\n")
            result = write_blog_post(topic, length)
            print(result)
            
        elif command == 'case_study':
            customer = sys.argv[2] if len(sys.argv) > 2 else 'Sample Customer'
            results = sys.argv[3] if len(sys.argv) > 3 else 'significant energy savings'
            print(f"📊 Creating case study for {customer}...\n")
            result = create_case_study(customer, results)
            print(result)
            
        elif command == 'calendar':
            duration = sys.argv[2] if len(sys.argv) > 2 else 'month'
            print(f"📅 Generating {duration} content calendar...\n")
            result = content_calendar(duration)
            print(result)
            
        elif command == 'campaign':
            goal = sys.argv[2] if len(sys.argv) > 2 else 'awareness'
            duration = sys.argv[3] if len(sys.argv) > 3 else 'week'
            print(f"🚀 Creating {duration} campaign for {goal}...\n")
            result = social_media_campaign(goal, duration)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: blog, case_study, calendar, campaign")
