# Vibe Coding Reflection: Example Excerpts

Use these two examples to show students the difference between surface-level and critically engaged reflection. Both respond to the same prompt — a 400-600 word reflection on using AI to generate code — but one demonstrates genuine thinking and the other does not.

---

## Generic Reflection (What to Avoid)

> Using AI to help with this project was a really interesting experience. The AI was very helpful in generating the code I needed, and it saved me a lot of time compared to writing everything from scratch. I was able to get a working result much faster than I would have on my own.
>
> I think AI is a powerful tool that can be used for good or bad depending on how you use it. When I used it responsibly, it helped me learn. There were a few times where I had to make changes to what it gave me, but overall it did a good job. I think the key is to use AI as a tool and not rely on it completely.
>
> In terms of ethics, I think it's important to cite when you use AI and to make sure you understand what it produces. AI can't replace human creativity and critical thinking. I plan to use AI in the future as a supplement to my own work, not as a replacement. I believe that as long as you are honest about using it and still put in effort, using AI is perfectly fine. Everyone should develop their own guidelines for how to use it responsibly.

### Why this doesn't work

- **No specifics.** There is not a single reference to what the AI actually generated, what language or framework was involved, or what the student changed. Every sentence could describe any project in any course.
- **No tension or difficulty.** The reflection presents the experience as frictionless. Nothing went wrong, nothing was confusing, nothing surprised them. That is either dishonest or unreflective.
- **Performed responsibility.** Phrases like "use AI as a tool" and "cite when you use AI" are correct positions, but they are stated as slogans rather than convictions. There is no evidence the student wrestled with any of these ideas.

---

## Strong Reflection (What to Aim For)

> The AI gave me a complete interactive dashboard on the first prompt -- a bar chart, a dropdown filter, and color-coded categories. Honestly, my first reaction was that I was done. It looked polished and it worked in the browser. But when I opened the JavaScript to change the color scheme, I realized I couldn't find where the colors were being set. The code used a D3 scale function I'd never seen before, and it took me about twenty minutes just to figure out that `scaleOrdinal` maps category names to colors from an array. I could have asked the AI to change the colors for me, but I wanted to understand the piece I was looking at.
>
> That moment is a good example of where I'd put myself on the understanding spectrum for this project: somewhere between "I can modify it" and "I can explain it." I can adjust pieces of the code now, but I wouldn't be able to build a D3 chart from a blank file. That gap bothers me a little. The AI was genuinely useful when I was stuck on layout -- I described what I wanted the page to look like and it generated clean CSS grid code that I could immediately read and adjust. But it was a problem when it produced a fetch call to load data from a JSON file, because I accepted it without understanding the async logic, and it broke when I reorganized my file structure. I spent more time debugging that than it would have taken to learn the basics.
>
> My personal rule going forward: if I can't explain a block of code to someone else in plain language, I don't get to keep it in my project without learning it first. That might slow me down, but the alternative is submitting work I can't defend.

### Why this works

- **Grounded in specifics.** The student names exact tools (D3, `scaleOrdinal`, CSS grid), describes a real sequence of events, and connects their reflection to concrete moments from the lab.
- **Honest about the gap.** Rather than claiming they understand everything or admitting nothing, the student locates themselves on the understanding spectrum and explains why that position is uncomfortable. This is genuine self-assessment.
- **The personal guideline has teeth.** "If I can't explain it, I don't get to keep it" is a real standard with a real cost (slower work). It reads as a conclusion the student arrived at through experience, not a platitude borrowed from a rubric.

---

## Discussion Prompts

After showing these examples, consider asking:

1. What specific details in the strong example make it convincing?
2. Could the generic example have been written without doing the lab at all?
3. Where would you place yourself on the understanding spectrum for code you have received from AI before?
