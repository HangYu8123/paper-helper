"""The patterns of the committee writing style reference.

Edit this file and run build_reference.py. The other .md files are generated.

Each pattern is one add(...) call:

    category   one of the six categories of Hang's writing style reference
    title      the heading of the pattern
    who        which writers show it: any of writer_a, writer_b, writer_c
    guidance   what the writers do
    forms      reusable wording, with [slots]
    fit        how the pattern relates to Hang's dissertation
    relation   same     Hang's reference already says this
               adds     Hang's reference has no pattern for this
               differs  Hang's preference differs and takes priority
    hang       titles of the related patterns in Hang's reference
    quotes     q(writer, PDF page, text). The build checks every quotation
               against the page text. [...] marks an omission.

In guidance and fit, {writer.measure} is replaced by a measured value, for
example {writer_a.sent_mean} or {draft.colon}. The measures are listed in
writer-profiles.md.

New patterns go at the end of their category.
"""

ENTRIES = []


def q(key, page, text):
    return dict(key=key, page=page, text=text)


def add(category, title, who, guidance, forms, fit, relation, hang, quotes):
    ENTRIES.append(dict(category=category, title=title, who=who.split(), guidance=guidance,
                        forms=forms, fit=fit, relation=relation, hang=hang, quotes=quotes))


# --------------------------------------------------------------------------- Vocabulary

add("Vocabulary", "Names for the document", "writer_a writer_b writer_c",
    "Each writer settles on a small set of names for the document and repeats them. Writer A writes this dissertation ({writer_a.n_this_dissertation} times in the chapters) and this work ({writer_a.n_this_work}), and also this dissertation work for what was done during the degree. Writer B writes this dissertation ({writer_b.n_this_dissertation}) and this work ({writer_b.n_this_work}). Writer C uses this dissertation and this thesis as equivalents ({writer_c.n_this_dissertation} and {writer_c.n_this_thesis}). None of them calls the document a paper.",
    ["This dissertation presents [contribution].",
     "In this work, [term] is defined as [definition].",
     "The remainder of this document is organized as follows.",
     "[Analysis or dataset] was [performed / collected] as part of this dissertation work."],
    "Keep this dissertation for the whole program and this chapter for one study, as Hang's reference already says. This work is common in all three and is acceptable for a short reference to the program. Choose dissertation or thesis and use only that one. A chapter that came from a paper should not call itself this paper.",
    "same", ["Impersonal dissertation voice", "Established dissertation terminology"],
    [q("writer_a", 19, "This dissertation presents a domain-independent computational model of moderation of multi-party human-machine interactions that enables a robot or virtual agent to act as a moderator in a group interaction."),
     q("writer_a", 26, "The remainder of this document is organized as follows:"),
     q("writer_a", 75, "The annotation and analyses described in the following sections were performed as part of this dissertation work."),
     q("writer_b", 9, "This dissertation suggests to embrace dynamic group conversations in HRI."),
     q("writer_c", 16, "Overall, this thesis approaches interaction by explicitly tackling representation alignment, rather than hoping it will naturally emerge.")])

add("Vocabulary", "Verbs for what a chapter does", "writer_a writer_b writer_c",
    "A chapter or the dissertation is the subject of a small set of verbs. Writer A uses presents, introduces, describes, reviews, and discusses. Writer B uses presents, describes, and reviews. Writer C, who writes with we, uses propose, present, introduce, formalize, and showcase. The verb says what kind of content follows, so reviews announces literature, introduces announces a new model or method, and presents announces a study or its results.",
    ["This chapter reviews [literature] in [fields].",
     "This chapter introduces [model or method], in which [one-clause description].",
     "This chapter presents [number] studies that [purpose].",
     "This chapter describes [system or procedure]."],
    "These verbs match the ones in Hang's reference. A chapter can present, introduce, review, or describe. It does not collect data or find results. Formalize promises a formal definition, so use it only where one follows.",
    "same", ["Research actions", "Impersonal dissertation voice"],
    [q("writer_a", 28, "This chapter reviews relevant literature in socially assistive robotics, computer supported collaborative work, and human-robot interaction."),
     q("writer_a", 118, "This chapter introduces the model of moderation and core moderation algorithm, in which the moderator monitors the interaction and takes actions to affect the social dynamics."),
     q("writer_b", 13, "This chapter reviews relevant background from social psychology."),
     q("writer_b", 25, "This chapter presents two experiments that we conducted to validate the idea that people establish group formations typical of human conversations with robots, and investigate various aspects of multi-party human-robot interactions."),
     q("writer_c", 131, "In this chapter, we formalize how autonomous systems can explicitly reason about how well they can explain given human inputs.")])

add("Vocabulary", "Develop, instantiate, validate, evaluate", "writer_a writer_b writer_c",
    "Writer A moves each contribution through a fixed chain of verbs. A model is formalized, an algorithm is developed from it, the algorithm is instantiated for one task, and the instance is validated or evaluated in a study. The same verbs return in every chapter opening and summary, so the reader always knows which step a sentence reports. Writer B uses designed and built for the platform, evaluated for a method on a benchmark, and validated for an idea that an experiment tests. Writer C uses test for hypotheses and showcase for a demonstration of a framework in one setting.",
    ["[Method] is instantiated for [task type] and evaluated in [study].",
     "[Idea] was validated in [setting] with [participants].",
     "[Framework] was evaluated on [benchmark or task] against [baselines]."],
    "Useful for the method chapters, where a general idea is followed by one implementation and one evaluation. Keep Hang's limit on validate, which needs a stated check. Evaluate does not say that the outcome was favorable.",
    "same", ["Research actions", "Method operations and their objects"],
    [q("writer_a", 135, "This algorithm is instantiated for collaborative tasks with individual goals, where the moderator either equalizes or reinforces performance on the task."),
     q("writer_a", 187, "Each of the four moderation algorithms described above was instantiated into a specific application domain, with domain-specific interaction features and objective functions, and then evaluated in that domain."),
     q("writer_b", 2, "We evaluate this framework in a public computer vision benchmark for group detection, and show how it can be used to estimate the members of a robot’s group conversation in real-time."),
     q("writer_c", 132, "we showcase the framework for learning from demonstrations using user demonstration data for an arm motion planning task;")])

add("Vocabulary", "Enable and leverage", "writer_a writer_b writer_c",
    "Enable is the shared verb for what the research makes possible for a robot or a person. It appears {writer_a.enable}, {writer_b.enable}, and {writer_c.enable} times per 1,000 words in Writer A, Writer B, and Writer C. Its object is an agent and an action, as in enable robots to detect. Leverage is rarer ({writer_a.leverage}, {writer_b.leverage}, and {writer_c.leverage} per 1,000 words) and means using something that already exists, such as a prior result, a dependency between two problems, or a dataset.",
    ["[Method] enables [agent] to [action] without [requirement].",
     "This chapter leverages [existing result or structure] to [purpose]."],
    "Both verbs are familiar to these readers, and leveraging is already in the title of the dissertation. Give enable an agent and an action. Hang's reference prefers the operation to a vague benefit, so follow enable with what the method does.",
    "same", ["Method operations and their objects", "Practical purpose"],
    [q("writer_a", 18, "The model of moderation provides a framework for developing algorithms that enable robots to moderate group interactions without the need for speech recognition"),
     q("writer_b", 46, "This chapter describes our efforts towards enabling robots to detect free-standing group conversations and their members."),
     q("writer_b", 46, "Here, we introduce an alternating optimization procedure to leverage the dependency between two problems to detect group conversations."),
     q("writer_c", 18, "In this third part, we enable the robot to automatically detect when its representation is misaligned with the human’s and fix it.")])

add("Vocabulary", "Insight, intuition, and observation", "writer_a writer_b writer_c",
    "The central idea of a method is named as an idea before it is implemented. Writer B writes our main insight is that and our key methodological insight. Writer C writes the core insight of this dissertation, the intuition is that, and our observation is that. Writer A uses insight for what a study yields, as in provides key insight into. The sentence that follows the label is short enough to remember and is repeated in the abstract, the chapter, and the conclusion.",
    ["The main insight of this chapter is that [relationship].",
     "The intuition is that if [condition], then [consequence].",
     "[Study] provides insight into [question]."],
    "This is the handoff from a finding to a method in Hang's reference. State the intuition once in a sentence and reuse that sentence. In the impersonal voice, the insight belongs to the chapter or the method.",
    "same", ["An intuition leading to an operation", "A study finding leading to a method"],
    [q("writer_a", 24, "The nutrition study provides key insight into how child-robot interactions develop over time, as well as providing insight for how a robot can use games to support cognitive skill development."),
     q("writer_b", 9, "Our main insight is that we can exploit the mutual dependency between two problems for this task."),
     q("writer_b", 10, "Our key methodological insight to reduce the bystander effect in this work was to design experimental protocols that assigned active roles to the participants."),
     q("writer_c", 18, "The intuition is that if a person decides two robot behaviors are similar, they must also internally represent them similarly, enabling us to extract their representation."),
     q("writer_c", 22, "Our observation is that many failures in robot learning, including the ones above, often result from a mismatch between the human’s representation and the one learned by the robot; in other words, their representations are misaligned.")])

add("Vocabulary", "People in the studies", "writer_a writer_b writer_c",
    "Participants is the word inside a study for all three. Outside a study the words differ by field. Writer A writes users, target users, and group members. Writer B writes people, users, and interactants. Writer C writes the human or the person for the teacher in a method, end-users for the people a system is built for, and non-expert users or novice users when experience matters. Each study states the number of participants, how they were recruited, and the limits of the sample.",
    ["[N] participants were recruited from [population].",
     "Participants experienced one of [N] conditions.",
     "Non-expert users can use [approach] to [teach / provide] [signal]."],
    "Hang's reference uses non-experts for the population, participants inside a study, demonstrators, and annotators. Writer C's non-expert users and novice users show that the term is familiar to this committee. Keep Hang's four terms and do not add novice as a synonym.",
    "same", ["Teachers and collection settings"],
    [q("writer_a", 59, "A key component of the development of any SAR system is understanding the target users population that the robot will be assisting."),
     q("writer_b", 27, "Twenty groups of 3 or 4 children interacted with Chester and Blink, for a total of 74 participants."),
     q("writer_c", 36, "In a user study with the JACO2 (Kinova) robotic arm, we show that non-expert users can use our approach for learning features (Sec. 3.5.2)."),
     q("writer_c", 54, "We recruited 12 users (11 male, aged 18-30) from the campus community to interact with our simulated JACO robot and provide feature traces for the three tasks.")])

add("Vocabulary", "Words for imperfect human input", "writer_c",
    "Writer C's dissertation is the closest of the three to Hang's topic. Input from non-experts is called noisy, and features learned from it are called noisy or imperfect. The loss relative to experts is called degradation in input quality or degradation in performance. The claim that follows is measured against two reference points, an expert and a random baseline. Noisy input is described as input that still carries signal.",
    ["[Non-expert input] was closer to [expert level] than to [random baseline] on [measure].",
     "When given imperfect [inputs], [method] still [outcome] relative to [baseline].",
     "With very noisy [inputs], the results are less conclusive."],
    "Hang's reference uses imperfections as the umbrella term and asks that noisy, sub-optimal, and unsuccessful each keep an operational definition. Writer C's wording supports the same stance, which is that imperfect teaching still contains information. The two reference points, expert and random, are a form worth reusing where the data allow it.",
    "same", ["Imperfect teaching and structured behavior", "Describing human teaching without blame"],
    [q("writer_c", 55, "While this does not mean that user features are as good as expert features (we expect some degradation in performance when going to non-experts), it shows that [...] the user features maintain a lot of signal despite this degradation."),
     q("writer_c", 68, "In online FERL where a single feature was missing, the structure captured by the (noisy) non-expert features was still helpful in learning a better reward than the baseline."),
     q("writer_c", 36, "Unfortunately, due to the current pandemic, we conducted the study online in a simulated environment; despite the inevitable degradation in input quality that this entails, the users were still able to teach features that induced informative bias."),
     q("writer_c", 61, "when given imperfect features, the learned reward is superior to trying to learn everything implicitly from demonstrations.")])

add("Vocabulary", "Graded words for evidence", "writer_a writer_b writer_c",
    "The strength of a finding is graded in words that sit next to the number. Writer A writes some support, limited evidence, modest evidence, preliminary evidence, marginal significance, and a trend towards. Writer B writes some evidence of and a trend suggested. Writer C writes provide evidence that, less conclusive, and less clear results. Strong words such as demonstrate and show are kept for results with a significant test or a clear margin.",
    ["[Analysis] provides preliminary evidence for [pattern].",
     "There was limited evidence that [outcome] (H[n]).",
     "[Result] showed a trend towards [direction] ([statistic]).",
     "The results are less conclusive when [condition]."],
    "This agrees with Hang's rule that claim strength follows the evidence. Put the value next to the graded word, as Hang's reference asks for correlations. Marginal significance and trend need the p value beside them.",
    "same", ["Hedges and degree words", "Reporting findings and interpretations"],
    [q("writer_a", 74, "In terms of the educational goal of the intervention, we find limited evidence that the children in the study learned about nutrition over the intervention"),
     q("writer_a", 74, "Finally, although we find that children take longer to make food selections over time, contrary to H4, we have modest evidence that children choose healthier foods over time, suggesting that the increase in time may be due to greater thoughtfulness in their responses."),
     q("writer_a", 94, "A post hoc analysis dividing the participants into two groups provides preliminary evidence for a spectrum of interpretations of a socially assistive robot among children with autism."),
     q("writer_b", 33, "We saw some evidence of F-formations [86], especially with older participants."),
     q("writer_c", 67, "Offline FERL similarly beats ME-IRL when the features used are of high enough quality, but the results are less conclusive when using very noisy features.")])

add("Vocabulary", "Suggest, may, might, could", "writer_a writer_b writer_c",
    "Interpretations are hedged with a small set of words, and each writer has favorites. Suggest and its forms appear {writer_a.suggest}, {writer_b.suggest}, and {writer_c.suggest} times per 1,000 words in Writer A, Writer B, and Writer C. May appears {writer_a.may}, {writer_b.may}, and {writer_c.may} times, might {writer_a.might}, {writer_b.might}, and {writer_c.might} times, and could {writer_a.could}, {writer_b.could}, and {writer_c.could} times. Writer A prefers might and suggesting that. Writer B prefers could and tend to. Writer C prefers may. Hang's draft has {draft.suggest} for suggest, {draft.may} for may, {draft.might} for might, and {draft.could} for could, which is inside the range of the three.",
    ["[Result], suggesting that [bounded interpretation].",
     "This finding might indicate [interpretation].",
     "[Group] tended to [behavior] when [condition]."],
    "Hang's reference gives each modal its own job, and the three dissertations use them the same way. No change in the amount of hedging is needed to match these readers. Keep the rule from the Chapter 8 review that can is not lowered to may as a matter of routine.",
    "same", ["Hedges and degree words"],
    [q("writer_a", 73, "We find that over the course of the intervention, children respond more quickly to the robot’s verbal queries, suggesting that they not only maintain engagement with the SAR system over time, but likely become more comfortable with the system, perhaps even building rapport with the robot character."),
     q("writer_b", 73, "These efforts to establish appropriate spatial arrangements suggest that people may be willing to collaborate with robots to establish F-formations and adapt to unforeseen circumstances."),
     q("writer_b", 74, "This finding might indicate more subtle effects of the manipulation than can be gleaned from questionnaires."),
     q("writer_c", 113, "Moreover, some users reported struggling to trade off the different features, which means that similarity queries might not be entirely preference-agnostic.")])

add("Vocabulary", "Prior work and efforts", "writer_a writer_b writer_c",
    "Prior work is the usual phrase in Writer A and Writer B, and Writer C titles a section Prior Work in most chapters. Writer B also writes prior efforts and calls her own research our efforts. Writer C names method families by their standing, such as traditional methods, typical methods, and state-of-the-art methods. A sentence about prior work says what the work focused on or assumed, so that the next sentence can state what it leaves open.",
    ["Prior work in [area] has primarily focused on [scope].",
     "Traditional [methods] rely on [assumption or representation].",
     "This chapter builds upon prior work on [topic]."],
    "Same phrase and same move as Hang's reference. Claims such as few studies and first still need literature support. Refer to Hang's own earlier studies by chapter.",
    "same", ["Prior work and research gaps"],
    [q("writer_a", 24, "Prior work in SAR has primarily focused on one-on-one interactions between robots and users: in many application domains, results from the social sciences suggest that individual attention from an assistive agent will better accomplish a user’s goals."),
     q("writer_b", 15, "Our efforts build upon this related work."),
     q("writer_b", 26, "A few prior efforts have explored the idea of companion or subordinate characters in HRI."),
     q("writer_c", 35, "In order to correctly interpret and efficiently learn from human input, traditional methods resorted to structuring the reward as a (linear) function of carefully hand-engineered features – important aspects of the task [311, 2, 144, 25].")])

add("Vocabulary", "Evaluative and emphatic words", "writer_a writer_b writer_c",
    "The three differ most in how much evaluation their words carry. Writer A is restrained and uses novel, key, and particular promise in a few places. Writer B uses essential and important for motivation and opens {writer_b.open_interestingly} sentences with Interestingly. Writer C is the most vivid, with notoriously challenging, vastly more complex, sorely needed, compelling evidence, and {writer_c.open_unfortunately} sentences that open with Unfortunately. In the passages read, the strong word is usually attached to a problem or a need, and less often to the writer's own result.",
    ["[Capability] is essential for [agents] to [goal].",
     "[Approach] has particular promise for [application].",
     "Selecting [object] is challenging, even for [experts], since [reason]."],
    "Hang's reference asks for value words used sparingly and next to the result that supports them. Writer A's restraint is the closest model. Writer C's stronger words are a personal register, and Hang's preference takes priority over it.",
    "differs", ["Value words and novelty", "Emphasis"],
    [q("writer_a", 23, "Socially Assistive Robotics has particular promise for supporting group interactions in assistive contexts."),
     q("writer_b", 46, "This ability is essential for these machine to adapt to the natural dynamics of social interactions and appropriately operate in human environments."),
     q("writer_c", 35, "Unfortunately, selecting the right feature representation is notoriously challenging, even for expert system designers: knowing and specifying a priori an exhaustive set of all the features that might be relevant for the reward is impossible for most real-world tasks."),
     q("writer_c", 196, "Despite these limitations, Boltzmann rationality has become so fundamental to how robots do inference and prediction, that designing a counterpart for continuous robotics domains is sorely needed.")])

# --------------------------------------------------------------------------- Wording preference

add("Wording preference", "First person and the impersonal voice", "writer_a writer_b writer_c",
    "This is the largest measured difference among the three, and between them and Hang's draft. We, our, and us appear {writer_a.we} times per 1,000 words in Writer A, {writer_b.we} in Writer B, and {writer_c.we} in Writer C. Hang's draft has {draft.we}. Writer A's abstract, introduction, chapter abstracts, and summaries are almost entirely impersonal, with this work, the model, and passive verbs as subjects, and we appears inside the study sections. Writer B and Writer C use we throughout, also for work by the single author. Writer C changes to I in the final chapter for her own plans. Writer B writes the author where she separates her part from a team's.",
    ["[Topic] is formalized as [problem] in which [description].",
     "This work presents [approach] that includes [parts].",
     "[Algorithm] is validated in [study], and it is shown that [result]."],
    "Hang's dissertation is impersonal by default and that decision stands. Writer A's dissertation shows the same voice in the framing parts, so a committee member's own writing supports it. Since all three use we in study sections, a remaining we in a procedure would not look unusual to these readers. It is still replaced under Hang's own rule.",
    "differs", ["Impersonal dissertation voice"],
    [q("writer_a", 20, "Moderation is formalized as a decision-making problem in which an agent in a multi-party interaction chooses social behaviors that change the interaction state, in order to maximize performance relative to both task goals and social goals."),
     q("writer_a", 135, "This instantiated algorithm is validated in peer group interactions, and it is shown that the moderator’s actions change both group cohesion and helpful behavior, depending on both how the moderator chooses which participant to help and how often the moderator addresses each participant."),
     q("writer_a", 61, "In order to move towards a longer intervention, we developed a 3-week long, twice-weekly intervention for first grade children, with a within-subjects design."),
     q("writer_b", 2, "In this work, we first develop a robotic platform for studying human-robot interactions, and contribute new experimental protocols to investigate group conversations with robots."),
     q("writer_b", 88, "The author contributed to designing and building parts of the robot, as well as setting up and integrating most software components."),
     q("writer_c", 197, "In this final chapter, I briefly outline a few future research directions towards such seamless human-robot interaction.")])

add("Wording preference", "A result with its test", "writer_a writer_b writer_c",
    "A quantitative result is one sentence that names the measure, gives the two values with their spread in parentheses, and gives the test with its statistic and p value. Writer A gives M and SD, the test, and often an effect size. Writer B gives the test in parentheses after the factor name and M and SE for each condition. Writer C names the test and its factors in words and gives F and p. The verb is plain, such as showed, revealed, was significant, or found.",
    ["Participants had higher [measure] in [condition A] (M = [a], SD = [b]) than in [condition B] (M = [c], SD = [d]).",
     "A [test] on [measure] showed [result] (p = [value]).",
     "[Factor] was significant ([statistic], p = [value])."],
    "Same content as Hang's reference, which asks for the measure, baseline, condition, and uncertainty together. Hang's reference uses compared with in a sentence and against inside parentheses. Do not add a test or a spread that the chapter did not compute.",
    "same", ["Numbers and measured comparisons", "A results paragraph answering one comparison"],
    [q("writer_a", 131, "Participants had higher scores on the group cohesion questionnaire in the moderated condition (M = 3.29, SD = 0.387) than in the unmoderated condition (M = 3.03, SD = 0.349)."),
     q("writer_a", 69, "A Cohen’s d statistic was also computed to measure this effect size (Cohen’s d = .57), which indicates a moderate intervention effect."),
     q("writer_b", 73, "Gaze was significant (F[1, 68] = 5.67, p = 0.02): participants stood significantly farther away from the robot with RG (M = 2.29, SE=0.05) than with AG (M = 2.09, SE = 0.06)."),
     q("writer_c", 55, "We ran an ANOVA with input type as a factor and task as a covariate, [...] finding a significant main effect (F(2, 103) = 132.7505, p < .0001).")])

add("Wording preference", "A difference that was not found", "writer_a writer_b writer_c",
    "A null result is reported as something the analysis did not find, and the sentence does not claim that the conditions are equal. Writer A writes we did not find significant differences and this trend did not reach statistical significance, and often adds a likely reason. Writer B writes was not significant and there were no significant differences. Writer C reports no significant difference and then says what the result does not mean.",
    ["No significant difference was found in [measure] between [conditions].",
     "[Trend with values], however this trend did not reach statistical significance.",
     "This does not mean that [A] is as good as [B]. It shows that [bounded statement]."],
    "Hang's preferred wording is did not detect a difference, with the warning that this does not mean the two conditions are equivalent. The three use find where Hang uses detect, and the stance is the same. Writer C's second sentence is the same warning written out.",
    "same", ["Reporting a difference that was not detected"],
    [q("writer_a", 68, "We did not find significant differences between the pre- and post-intervention ratings, as seen in Figure 4.3, likely due to the extremely high positive evaluation."),
     q("writer_a", 70, "There was a 2.29 mean increase in utterance length from the start to end of the intervention period, in accordance with H3, however this trend did not reach statistical significance."),
     q("writer_b", 34, "We did not find significant differences on how much participants touched the robot between Conditions, but there were differences between Age Groups."),
     q("writer_b", 33, "Condition was not significant, nor any interactions with Condition."),
     q("writer_c", 55, "which showed that the MSE for Random input was significantly higher than both Expert (p < .0001) and User (p < .0001), and found no significant difference between Expert and User (p = .0964).")])

add("Wording preference", "Hypotheses and verdicts", "writer_a writer_b writer_c",
    "Hypotheses are numbered and stated before the results. The verdict is attached to the result that decides it, with supporting H1, in line with H2, contrary to H4, or a label in parentheses such as H6 and H7 unsupported. Partial support is said in words. Writer A separates the part of a hypothesis that held from the part that did not. Writer C adds a caution to a supported hypothesis when the evidence for one part is weaker.",
    ["[Result with statistic], supporting H[n].",
     "Thus the first part of H[n], [content], is supported, but not [the second part].",
     "These results support H[n], although the evidence for [part] is weaker.",
     "No support was found for the hypothesis that [content]."],
    "Same practice as Hang's reference. Keep the verdict in the sentence that reports the deciding result, which matches Hang's preference for keeping a result and its interpretation together.",
    "same", ["Hypotheses and verdicts", "A short verdict after the evidence"],
    [q("writer_a", 68, "Thus the first part of H1, the positive perception of the robot, is supported, but not that there is an increase in this perception over the duration of the intervention."),
     q("writer_a", 132, "However, we did not find support for the hypothesis that the moderator robot would decrease participants’ negative attitudes towards robots."),
     q("writer_b", 73, "This result supported our first hypothesis (H1) and is related to prior findings on the influence of gaze on the perception of a robot’s head motion [107]."),
     q("writer_c", 55, "These results support H5, although the evidence for finding the teaching protocol intuitive is weaker, and participants might have a bias to be positive given they are in a study.")])

add("Wording preference", "Possible explanations", "writer_a writer_b writer_c",
    "An unexpected or weak result is followed by one or two candidate reasons, each marked as a possibility. Writer A writes this may have been because and may have been due to the fact that, and likely due to for the reason she finds most plausible. Writer B writes could be attributed to the fact that, an alternative explanation is that, and part of the problem could have been. Writer C writes it is unclear whether and names the two readings that the data cannot separate.",
    ["This may have been because [reason A], or may have been due to [reason B].",
     "[Result] could be attributed to [reason]. An alternative explanation is that [reason].",
     "It is unclear whether [outcome] is due to [A] or to [B]."],
    "Same as Hang's reference, which presents reasons as hypotheses that could be examined. Writer C's it is unclear whether is a useful form when two explanations remain open.",
    "same", ["Possible explanations", "An unexpected result and possible reasons"],
    [q("writer_a", 132, "This may have been because many of the participants had low scores on the NARS (especially the interaction subscale) initially, or may have been due to the fact that the interaction was centered on human-human interaction, not human-robot interaction."),
     q("writer_b", 44, "The bigger separation between the robot and the participants that we observed in the experiment could be attributed to the fact that Chester is different – it is a robot, not a person."),
     q("writer_b", 44, "An alternative explanation is that Chester’s face is planar."),
     q("writer_c", 196, "Moreover, although our experiments in Sec. 9.3.3 reveal that LESS still performs better inference than Boltzmann, it is unclear whether this outcome is due to the effect of hypothesis H3 or if our method is truly unaffected by misalignment.")])

add("Wording preference", "Limitations stated plainly", "writer_a writer_b writer_c",
    "A limitation is announced in a short sentence and then listed with its consequence. Writer B opens a discussion with the experiment was limited in several ways and counts the limits with First, Second, and Third. Writer A names the sample size, the interaction time, and the measure used as a proxy. Writer C states who the participants were and cautions that the result speaks to that population. The limit is tied to the design, and the writer does not apologize for it.",
    ["The [study] was limited in several ways. First, [limit]. Second, [limit].",
     "All [participants] had [property], so the results speak to [this population] and not to [the general population].",
     "This study has a small number of participants and [other constraint]."],
    "Same as Hang's reference, where a limitation names the design constraint and the claim it limits. Writer C's caution about a technical sample is a model for the studies with recruited non-experts and crowdworkers.",
    "same", ["Limitations and future work"],
    [q("writer_a", 97, "This study, like most, features a small number of participants and a limited amount of total interaction time with those participants (Scassellati et al., 2012)."),
     q("writer_a", 97, "Other limitations of the study include the use of head orientation as an imperfect proxy for attention; future work would benefit from modern gaze-tracking hardware."),
     q("writer_b", 35, "The experiment was limited in several ways."),
     q("writer_b", 87, "Our work was limited by our simulated environment."),
     q("writer_c", 54, "All users had technical background, so we caution that our results will speak to FERL’s usability with this population rather than the general population.")])

add("Wording preference", "Wording for future work", "writer_a writer_b writer_c",
    "Future work is written with a modal that shows how firm the plan is. Writer A uses might, would, and could, and further research is needed to determine whether for an open question. Writer B uses it would be interesting to explore and should. Writer C uses must for a gap in her own method, could for an option, and I plan to in the final chapter for work she intends to do. A direction is stated together with what it would make possible.",
    ["Further research is needed to determine whether [question].",
     "Future work could [action], which would [benefit].",
     "One possible direction for future work is [topic]. Another area of future work is [topic]."],
    "Hang's reference uses Future work could and One planned step is to, with would for what a planned study does. Writer C's I plan to shows that planned work stated as a plan is accepted in a final chapter, and in Hang's impersonal voice this is one planned step. Write only what Hang's notes say.",
    "same", ["Limitations and future work", "Future work drafted from notes"],
    [q("writer_a", 152, "Further research is needed to determine whether the long-term social benefits of a robot moderator offset short-term decreases in task performance."),
     q("writer_a", 188, "Future research might directly model the dynamics of the interaction in order to enable the moderator to take appropriate turns and make decisions about whether or not the moderator’s intervention is needed."),
     q("writer_b", 89, "Moving forward, it would be interesting to explore data-driven approaches to enable robots to reason about human spatial behavior."),
     q("writer_b", 90, "Future work should explore the problem of robot localization in crowded environments further to unlock human-robot interactions in busy human gatherings."),
     q("writer_c", 69, "Future work must investigate ways in which the robot can determine whether to accept or reject the newly learned feature."),
     q("writer_c", 198, "In the future, I plan to study other such proxy tasks, and even leverage unsupervised pre-training methods for improving sample efficiency.")])

add("Wording preference", "Contribution statements", "writer_a writer_b writer_c",
    "Contributions are a list with a lead-in sentence. Writer A separates primary contributions from secondary ones and writes each as a noun phrase. Writer B gives two take-home messages as full sentences and then a list of contributions with a label and a pointer to the chapter. Writer C lists contributions inside each chapter and starts each one with a verb. All three end the lead-in with a colon.",
    ["The following are the primary contributions of the dissertation:",
     "A [type of contribution] of [object] wherein [what it does].",
     "[Label]. [One sentence on what was built or shown] ([chapter])."],
    "Hang's Introduction has a Contributions section, and Hang's reference asks that a contribution be distinct from an aspiration. Writer A's split between primary and secondary contributions could hold the datasets and code. A colon after a complete lead-in to a list is the case that Hang's reference keeps.",
    "same", ["Contribution statements", "Few colons and semicolons"],
    [q("writer_a", 25, "The following are the primary contributions of the dissertation:"),
     q("writer_a", 25, "A computational formalization of moderation wherein an agent optimizes for the achievement of multiple social and task goals in an interaction."),
     q("writer_b", 88, "The main take-home messages of this dissertation are:"),
     q("writer_b", 88, "We built a new platform for social HRI research (Chapter 4)."),
     q("writer_c", 132, "we introduce a general framework for quantifying representation misalignment when the human and the robot are acting on the same dynamical system;")])

add("Wording preference", "Definitions in a full sentence", "writer_a writer_b writer_c",
    "A term is defined in its own sentence when it first matters. Writer A writes is defined in this work as and we define, and repeats the definition in the abstract, the introduction, and the chapter that uses it. Writer B writes a plain is sentence. Writer C introduces a new term with which we call and a dash followed by the definition. The defined term is then used without variation.",
    ["[Term] is defined in this work as [definition].",
     "A [term] is a [category] that [distinguishing property].",
     "[Description of the new object], which is called [term] in this dissertation."],
    "Same as Hang's reference, which defines the signal before notation. Writer A's phrase in this work limits the definition to the dissertation, which fits progress and the feedback terms. Writer C's dash can be written as a which clause.",
    "same", ["Definitions before notation", "Established dissertation terminology"],
    [q("writer_a", 17, "A moderator is defined in this work as an agent that regulates social and task outcomes in a goal-oriented social interaction."),
     q("writer_a", 119, "We define the moderator as a member of a goal-directed multi-party interaction whose role is to regulate the behavior of the other participants."),
     q("writer_b", 25, "A sidekick is a character that is closely associated with another primary character, and regarded as a subordinate or partner."),
     q("writer_c", 35, "We introduce a new type of representation-specific human input specifically designed to teach features, which we call feature traces – partial trajectories that describe the monotonic evolution of the value of the feature to be learned.")])

add("Wording preference", "Scope statements", "writer_a writer_b writer_c",
    "Each writer says what the dissertation does not cover, early and in one or two sentences. Writer B writes we limit the scope of this dissertation to and is out of the scope of this dissertation. Writer A writes is not directly addressed in this work and separates her topic from a neighboring one. Writer C states where a method was shown and where else it could apply. The excluded topic often returns as future work.",
    ["The scope of this dissertation is limited to [setting or population].",
     "[Topic] is not directly addressed in this dissertation.",
     "[Term A] is distinguished from [term B], since [the model] applies only to [condition].",
     "Although evaluated in [domain], [method] can be used in [other settings] where [condition]."],
    "Hang's reference has no separate pattern for scope, so this one adds to it. A scope sentence in the Introduction answers a question that a committee member would otherwise ask at the defense. The last form states an expectation and needs could or can be expected to unless it was tested.",
    "adds", ["Conditions attached to benefits"],
    [q("writer_a", 119, "We also distinguish moderation from mediation: our model applies only to interactions where the goals of the group members are not in conflict."),
     q("writer_a", 188, "The problem of when to moderate is not directly addressed in this work."),
     q("writer_b", 10, "We limit the scope of this dissertation to studying spatial behavior typical of group conversations were people are standing and quasi-static, as it often happens during social encounters in public, open spaces."),
     q("writer_b", 10, "However, studying these interactions and other modalities of communication is out of the scope of this dissertation."),
     q("writer_c", 36, "Although showcased in manipulation, our method can be used in any robot learning scenarios where feature learning is beneficial: in collaborative manufacturing users might care about the rotation of the object handed over, or in autonomous driving passengers may care about how fast to drive through curves.")])

add("Wording preference", "Where the work was published and who did it", "writer_a writer_b writer_c",
    "All three say where the content of a chapter appeared and who contributed. Writer C opens each chapter between the introduction and the conclusion with a line that names the papers and the collaborators. Writer B names the venue in the outline and again at the start of several chapters. Writer A names the collaborating institutions and the venue in the section, and marks which part was performed as part of this dissertation work when the data came from others.",
    ["This chapter is based on [paper], written in collaboration with [names].",
     "The work presented in this chapter was originally published as [title].",
     "The [data collection] was performed by [others]. The [analysis] was performed as part of this dissertation work."],
    "Hang's published study chapters already carry the second form. Where a chapter uses data or systems from collaborators, Writer A's two sentences state the division clearly. Hang's rule of citing chapters and not Hang's own papers concerns cross-references and is not affected.",
    "same", ["Prior work and research gaps"],
    [q("writer_a", 60, "The work described in this section was performed collaboratively with researchers at the Massachusetts Institute of Technology, Yale University, and Stanford University, and was published in the 23rd IEEE International Symposium on Robot and Human Interactive Communication"),
     q("writer_a", 75, "The annotation and analyses described in the following sections were performed as part of this dissertation work."),
     q("writer_b", 25, "A publication about this work appeared in the 2014 ACM/IEEE International Conference on Human-Robot Interaction [197]."),
     q("writer_b", 46, "The proposed approach was first published in IROS’15 [199]."),
     q("writer_c", 34, "This chapter is based on the papers “Feature Expansive Reward Learning: Rethinking Human Input” [40] and “Inducing Structure in Reward Learning by Learning Features” [41], written in collaboration with Marius Wiggert, Claire Tomlin, and Anca Dragan.")])

add("Wording preference", "Pointing to figures, sections, and chapters", "writer_a writer_b writer_c",
    "The introduction of each dissertation has one figure that shows the whole approach, and the text points to it. Writer A's figure shows the overall approach, Writer B's shows the research methodology, and Writer C's places every chapter in one diagram. Inside chapters, a figure is named as the place where something is seen or summarized, and a result often ends with the figure in parentheses. Other parts of the dissertation are cited by number.",
    ["This approach is summarized in [figure].",
     "[Statement], as seen in [figure].",
     "[Result] ([figure]).",
     "[Object] is described in [section]."],
    "Hang's Introduction has an overview figure, which matches all three. Hang's reference asks for chapter labels in place of typed numbers, which LaTeX references provide.",
    "adds", ["Established dissertation terminology", "Parentheses for supporting specifics"],
    [q("writer_a", 20, "This approach is summarized in Figure 1.1."),
     q("writer_a", 114, "These insights were used to develop a cooperation-focused robot control algorithm, described in Section 7.1."),
     q("writer_b", 11, "We use an iterative research methodology, as depicted in Figure 1.2, to study social group conversations, develop new robot capabilities, and evaluate the effectiveness of the proposed approaches for HRI."),
     q("writer_c", 16, "Fig. 1.1 provides a visual overview of the four main parts of the thesis (which we briefly motivate below) and how they fit in the broader space of representation alignment in human-robot interaction.")])

# --------------------------------------------------------------------------- Writing style

add("Writing style", "A concrete scene before the abstraction", "writer_a writer_b writer_c",
    "A problem is shown in a small scene before it is named in general terms. Writer B asks the reader to consider a figure in which two people talk near a robot. Writer C uses a robot that hands a user a cup of coffee. Writer A gives two users who respond differently to the same request. The scene takes one to three sentences and is followed by the general statement it illustrates.",
    ["For example, consider [figure], in which [situation].",
     "To [goal], the robot [considers / needs] [quantities]. [What goes wrong without them].",
     "One user might [response A], while another might [response B]."],
    "Same as the hypothetical scenario in Hang's reference. Label a hypothetical case as one, keep it short, and return to the technical point.",
    "same", ["A hypothetical scenario that explains a problem", "An example in a few connected sentences"],
    [q("writer_a", 188, "Especially as robots move into homes and long-term interactions, it may become necessary to personalize the robot’s behavior to the preferences of the individual: one user might be more likely to take the robot’s suggestion if asked nicely, while another might prefer the robot to be more firm."),
     q("writer_b", 8, "For example, consider Figure 1.1a in which two people talk to each other."),
     q("writer_b", 90, "For example, imagine being at a loud party."),
     q("writer_c", 15, "To act in the world, robots rely on a representation of salient features of the task: for instance, to hand a user a cup of coffee, the robot may consider movement efficiency and cup orientation in its behavior.")])

add("Writing style", "One example carried through", "writer_b writer_c",
    "Writer C returns to one household scene, a robot that carries a cup near a laptop, in the introduction and in most chapters. Each new idea is explained by changing one detail of that scene, with phrases such as in our earlier example and in the above example. Writer B does the same with her robot and its named behaviors. The reader learns the example once and afterwards attends only to what changed.",
    ["In the earlier example, if [changed condition], [consequence].",
     "In the scenario in [figure], [actor] wants [goal]."],
    "Hang's chapters use different tasks, so one example for the whole dissertation is not available. Inside a chapter, the task of that chapter can serve as the running example for the signal, the method, and the result.",
    "adds", ["An example in a few connected sentences"],
    [q("writer_b", 25, "In this experiment, we made Chester the main character and Blink its sidekick."),
     q("writer_c", 34, "For instance, in the scenario in Fig. 3.1, the human wants the robot to keep the cup away from the laptop to prevent spilling liquid over it; she may communicate this preference to the robot by providing a demonstration of the task or even by directly intervening during the robot’s task execution to correct it."),
     q("writer_c", 35, "In our earlier example, if the robot were taught about the concept of distances to laptops separately, it would be able to quickly tell what the person wants from a single demonstration."),
     q("writer_c", 16, "In the above example, a user might care about how close to them the robot moves or whether it carries the mugful of coffee around their expensive laptop, and what “close” or “around” means will differ from person to person and be context-dependent.")])

add("Writing style", "The gap, then the response", "writer_a writer_b writer_c",
    "The motivation names what existing work covers, what it leaves out, and why. Writer B writes that a problem has often been overlooked, lists the related problems that have been studied, and gives a reason for the gap. Writer C states what typical methods do, the limit of that approach, and the alternative introduced by Instead. Writer A states what prior work has primarily focused on and the case in which that focus does not hold. The gap is specific, and prior work is described without dismissal.",
    ["[Problem] has often been overlooked by [community]. However, these methods do not address [specific problem]. One reason for this gap is [reason].",
     "Typical methods [approach], but [limit]. Instead, [alternative].",
     "Prior work in [area] has primarily focused on [scope]. There are exceptions, however, when [condition]."],
    "Same as the introduction pattern in Hang's reference, which is built around a particular assumption about human teaching. Writer B's third sentence, the reason for the gap, is a useful addition.",
    "same", ["An introduction built around a consequential assumption", "Prior work and research gaps"],
    [q("writer_a", 24, "There are exceptions to this, however, when fostering social interactions between people is a goal of the system."),
     q("writer_b", 8, "The problem of detecting social conversations and their members has often been overlooked by the HRI community."),
     q("writer_b", 9, "One reason for this gap is the heavy focus of the community on studying one-on-one human-robot interactions."),
     q("writer_c", 16, "Typical methods attempt to learn the human’s representation of what matters in a task from aggregated data sets of human behavior, but this data will also not reflect every individual, environment, and task the robot will be exposed to."),
     q("writer_c", 16, "Instead, we suggest that we should treat humans as active participants in the interaction not as static data sources.")])

add("Writing style", "The thesis in one sentence", "writer_a writer_b writer_c",
    "Each dissertation can be reduced to one sentence, and the writer provides it. Writer B sets the goal of the dissertation apart from the paragraph. Writer C sets the core insight apart in the same way. Writer A opens the abstract with the sentence and repeats it word for word in the introduction. The sentence names the object, such as a model or computational models, and what it makes possible.",
    ["The goal of this dissertation is to [verb] [object] for [purpose].",
     "This dissertation presents [object] that enables [agent] to [action]."],
    "This adds to Hang's reference. Check that the Abstract, the Overview, and the Conclusion state the thesis in the same words, and that the three stages follow from it.",
    "adds", ["The three stage dissertation arc"],
    [q("writer_a", 17, "This dissertation presents a domain-independent computational model of moderation of multi-party human-machine interactions that enables a robot or virtual agent to act as a moderator in a group interaction."),
     q("writer_b", 9, "the goal of this dissertation is to develop computational models for robots to detect and sustain the spatial patterns of human behavior that naturally emerge during free-standing group conversations."),
     q("writer_c", 16, "successful human-robot interaction requires robots to engage with humans in an interactive process for finding a shared representation of what’s salient for the task.")])

add("Writing style", "Research as iteration", "writer_a writer_b writer_c",
    "The dissertation is presented as a cycle of studying people, building a capability, and evaluating it. Writer A calls this an iterative approach and Writer B an iterative research methodology, and both show it in a figure. Each study is said to inform, motivate, or enable the next step. A limitation observed in one study is named as the reason for the following chapter.",
    ["The results of this study motivate [next step].",
     "This limitation motivated [the work in the next chapter].",
     "These studies inform the development of [method or behavior]."],
    "Hang's three stages, understand, mitigate, and leverage, are the same kind of story. Hang's reference adds a boundary, which is that a study can motivate a method without validating it, and that the stages are a conceptual dependency.",
    "same", ["The three stage dissertation arc", "A study finding leading to a method"],
    [q("writer_a", 20, "This work presents an iterative approach to developing the model of moderation, that includes studies and analyses to develop an understanding of the application domains for robot moderators that inform the development of algorithms based on our model of moderation."),
     q("writer_a", 74, "The results of this study motivate our subsequent work on developing SAR interactions that support cognitive skill development in children."),
     q("writer_b", 11, "This methodology also drives the organization of the rest of this document."),
     q("writer_b", 45, "This limitation motivated us to work towards enabling robots to automatically detect nearby conversational groups."),
     q("writer_c", 56, "In the following sections, we explore whether both expert and non-expert features can be used to improve reward learning generalization.")])

add("Writing style", "Implications for other researchers", "writer_a writer_b writer_c",
    "A discussion says what the result means for people who build or study similar systems. Writer A addresses designers and researchers directly and says under which goal a design choice is preferable. Writer B states that the work has design implications and that a protocol could be used to study other questions. Writer C titles paragraphs Implications for a named setting. The implication is conditional on a goal or a setting.",
    ["For [designers / researchers] of [systems], these results [suggest / provide] [implication].",
     "For scenarios where [goal] is most important, [design choice] may be preferable.",
     "[Protocol or method] could be used to study [other question]."],
    "This matches the practical purpose and the methodological implication in Hang's reference. Keep could and may for uses that were not tested.",
    "same", ["Practical purpose", "Discussion synthesis and its boundary"],
    [q("writer_a", 95, "For designers of SAR systems and researchers in SAR for children with autism, these results provides important insights for future work."),
     q("writer_a", 95, "For scenarios where children’s enjoyment of interactions (as measured by responsiveness and positive affect) is most important, these outcomes may be maximized when the behavioral and morphological agency of the robot is matched to the developmental level of the target sub-population of children with autism."),
     q("writer_b", 36, "Our work has design implications."),
     q("writer_b", 74, "The brainstorming protocol could be used to study other aspects of HRI."),
     q("writer_c", 67, "Our online FERL approach provides an alternative that allows people to teach features when the robot detects it is missing something, and then update the reward using the new feature set.")])

add("Writing style", "Observations and participants' words", "writer_a writer_b writer_c",
    "Numbers are accompanied by what was seen and what participants said. Writer A reports observations with we observed and quotes single words and remarks. Writer B quotes children's utterances and describes one session frame by frame in a figure. Writer C quotes written remarks from the survey in parentheses after the result they explain. The quotation is short, is attributed to one participant or several, and supports a point that the numbers already make.",
    ["Participants [general observation], and in the words of one participant, [quoted remark].",
     "Several participants mentioned that [content] ([quoted remark]).",
     "For example, one participant [action or remark], which illustrates [pattern]."],
    "Same as the observed episode in Hang's reference. Use only episodes and remarks that the study recorded, and do not treat one remark as evidence of how common something is.",
    "same", ["An observed episode in action order"],
    [q("writer_a", 132, "We observed that overall participants had a positive interaction with the robot, finding it engaging and, in the words of one participant, “cute”."),
     q("writer_a", 71, "For example, one child began his interaction with “yeah” and “maybe,” and proceeded to recall what the robot had said in a previous session and said “you said you don’t like mashed potatoes!”, demonstrating both relational speech and, given the tone of the interaction, humor with the robot."),
     q("writer_b", 35, "For example, one participant said the following when Chester was about to turn: “I feel bad for the lamp. I hope you are going to be OK”."),
     q("writer_c", 55, "In fact, several participants mentioned in their additional remarks that they had a good idea of what traces to give, and the only frustrating part was the GUI interface")])

add("Writing style", "Candor about costs", "writer_a writer_b writer_c",
    "All three say plainly when something did not work or came at a cost. Writer A reports that the robot's assistance did come at a cost and gives the lower task performance. Writer B writes Unfortunately when a difference was too small to interpret, and of course, we pay a price for a method's flexibility. Writer C writes that a method is not the full answer and lists what it does not solve. The admission is specific and is followed by what can still be concluded.",
    ["However, [benefit] did come at a cost, since [measured cost].",
     "This difference was small enough that it had no functional meaning.",
     "[Method] does not solve [problem] fully. [What it improves]."],
    "This adds to Hang's reference. It fits the dissertation's own argument, since imperfect teaching is its subject. Writer C's idioms are replaced by literal wording under Hang's rule.",
    "adds", ["Literal wording", "An unexpected result and possible reasons"],
    [q("writer_a", 152, "However, the robot’s assistance did come at a cost: the performance of the group was higher in the unmoderated testing sessions (H6 and H7 unsupported)"),
     q("writer_b", 44, "Unfortunately, this difference was small enough, that we thought it had no functional meaning."),
     q("writer_b", 87, "Of course, we pay a price for this flexibility: the more complex the state is, the more data RL methods need to learn from."),
     q("writer_c", 125, "That said, we need to be explicit that this is not the be-all end-all solution to our goal above."),
     q("writer_c", 125, "The learned rewards are not perfect — they are just better than alternatives.")])

add("Writing style", "A step, not an end point", "writer_a writer_b writer_c",
    "The size of the contribution is stated modestly. Writer B calls the dissertation our first steps toward a research agenda. Writer C calls a chapter merely a step towards understanding and a step towards recovering what she wants to recover. Writer A says that results provide a basis for further algorithms and that evidence is preliminary. The modest frame is paired with a clear statement of what was shown.",
    ["[Work] is a step towards [larger goal].",
     "These results provide a basis for [next development]."],
    "This agrees with Hang's restraint on novelty claims. One such sentence in a chapter is enough, and it should not replace the statement of the finding.",
    "same", ["Value words and novelty"],
    [q("writer_a", 134, "These results support the use of a robot as the moderator in a group interaction, and provide a basis for the development of further moderation algorithms."),
     q("writer_b", 88, "This dissertation presented our first steps toward a research agenda where we aim to make robot perception cognizant of social behavior for HRI."),
     q("writer_c", 68, "Our work is merely a step towards understanding how explicitly focusing on learning features can impact reward learning generalization and sample complexity."),
     q("writer_c", 126, "Overall, similarity queries are a step towards recovering human-aligned representations.")])

add("Writing style", "Register", "writer_a writer_b writer_c",
    "Writer A and Writer B write in a formal register throughout. Writer C mixes a formal register with conversational touches, such as contractions, idioms, and questions to the reader. Contractions appear {writer_a.contraction}, {writer_b.contraction}, and {writer_c.contraction} times per 1,000 words in Writer A, Writer B, and Writer C. All of Writer A's are inside the quoted speech of participants or of the robot, and Writer B has a few of her own. Writer C's idioms include from the get-go and the be-all end-all solution.",
    ["[Subject] is modeled as [formal description], in which [components].",
     "This dependency implies that [consequence]."],
    "Hang's reference asks for literal wording, and Hang's draft has no contractions. That is the register of Writer A and Writer B. Writer C's conversational touches are her own voice and are not a model for this dissertation.",
    "differs", ["Literal wording"],
    [q("writer_a", 119, "In this work, moderation is modeled as a cyclic decision-making process, in which the moderator monitors the interaction state, evaluates the state relative to some number of task and social goals, and chooses social behaviors that change the interaction."),
     q("writer_b", 74, "This dependency implies that robots should reason about and control their gaze and body motion jointly."),
     q("writer_c", 17, "So far, we assumed that the human can identify every individual feature of the representation they wish to teach, but that’s not always easy."),
     q("writer_c", 36, "First, we look at an easier online reward learning setting like the one in Fig. 3.1 (Right-Top) where the robot knows part of the feature set from the get-go, but the person’s preference also depends on other features not in the set (Sec. 3.4.2).")])

add("Writing style", "Ending on the wider stake", "writer_a writer_b writer_c",
    "The last paragraph of each dissertation leaves the technical content and states what the work is for. Writer A ends with an ethical concern of her field and how her approach answers it. Writer B ends a future direction with what it could teach about human conversation. Writer C ends by asking a broader research question and describing the systems that would benefit. The closing is short and is not a summary.",
    ["One consistent concern in [field] is that [concern]. This dissertation demonstrates another path, which is [approach].",
     "Ultimately, these efforts could help [wider benefit]."],
    "Hang's Conclusion closes with the hope that future work will embrace the imperfections in non-expert teaching, which is this move. Writer A's closing names a concern of the field and says how her approach answers it. The content of a closing has to come from Hang. A closing for the whole dissertation does not conflict with Hang's rule against adding a closing sentence to each future-work paragraph.",
    "adds", ["Future work drafted from notes", "Practical purpose"],
    [q("writer_a", 189, "One consistent area of ethical concern in socially assistive robotics is that the robot interaction partner will replace human-human contact and further isolate vulnerable users."),
     q("writer_a", 189, "This approach allows the richness of the interaction to come from the relationships between human users, and supports people in turning towards each other rather than away."),
     q("writer_b", 89, "Ultimately, these efforts could help us better understand human conversations."),
     q("writer_c", 197, "This opens up a broader research question: how can robots help the human-robot team converge to a shared representation?")])

# --------------------------------------------------------------------------- Sentence style

add("Sentence style", "Sentence length", "writer_a writer_b writer_c",
    "The three write sentences of different lengths, and Hang's draft is within their range. The mean is {writer_a.sent_mean} words in Writer A, {writer_b.sent_mean} in Writer B, and {writer_c.sent_mean} in Writer C, against {draft.sent_mean} in Hang's draft. Sentences of 35 words or more make up {writer_a.long_share} percent of Writer A's, {writer_b.long_share} percent of Writer B's, and {writer_c.long_share} percent of Writer C's, against {draft.long_share} percent of the draft's. Writer A's long sentences carry a result with its conditions and its interpretation. Writer B breaks the same content into two or three sentences. All three place a short sentence where a point has to stand out.",
    ["[Short statement of the point]. [Longer sentence with the evidence and its condition].",
     "One possible direction for future work is [topic]."],
    "No change in sentence length is needed to suit these readers. Hang's rule of one main job for each sentence decides where to split, and a result stays with the which clause that interprets it.",
    "same", ["One main job and varied sentence length"],
    [q("writer_a", 188, "One possible direction for future work is personalized moderation."),
     q("writer_a", 118, "For this work, we primarily use time-based approaches to choosing when the robot should act, and focus on algorithms for selecting robot behaviors in order to achieve both task-related and social goals in the interaction."),
     q("writer_b", 34, "This analysis was inconclusive and there were no significant differences."),
     q("writer_b", 2, "Lower-body orientation is a key descriptor of spatial behavior and, thus, can help detect group conversations."),
     q("writer_c", 18, "Human behavior is not random – it is intentional and reflective of internal goals and preferences.")])

add("Sentence style", "A short sentence that states the point", "writer_a writer_b writer_c",
    "A paragraph often begins with a short declarative sentence that says what the paragraph establishes. Writer B sets this sentence in small capitals at the start of most discussion paragraphs, so that a discussion can be read from these sentences alone. Writer C and Writer A use the same kind of sentence without the typography. The sentence is a claim or a finding and has a subject and a verb.",
    ["[Factor] had effects on [outcome].",
     "There were no differences in [measure] between conditions.",
     "The quality of [output] depends directly on the quality of [input]."],
    "Hang's reference asks for discussion headings with a concrete subject. Writer B's lead sentences are a second way to do this without adding headings. A lead sentence must not claim more than the paragraph shows.",
    "same", ["Headings that name the question or finding", "Direct subjects and concrete details"],
    [q("writer_a", 97, "Challenges inherent in performing studies involving children with autism are well established."),
     q("writer_b", 35, "The sidekick had effects on the interaction."),
     q("writer_b", 74, "Robot gaze and orientation can affect users’ perception of these behaviors."),
     q("writer_b", 87, "Our findings suggest that RL has potential to succeed in motion control tasks during social conversations."),
     q("writer_c", 68, "The quality of the learned rewards depends directly on the quality of the learned features.")])

add("Sentence style", "Openers that mark the step", "writer_a writer_b writer_c",
    "Sentences often open with a word that tells the reader how the sentence relates to the one before. However opens {writer_a.open_however} sentences in Writer A, {writer_b.open_however} in Writer B, and {writer_c.open_however} in Writer C. Writer A's other frequent openers are Additionally ({writer_a.open_additionally}) and Finally ({writer_a.open_finally}). Writer B's are For example ({writer_b.open_for_example}), In general ({writer_b.open_in_general}), In particular ({writer_b.open_in_particular}), and Moreover ({writer_b.open_moreover}). Writer C's are Unfortunately ({writer_c.open_unfortunately}), Lastly ({writer_c.open_lastly}), and For example ({writer_c.open_for_example}). The last item of a series is marked with Finally or Lastly.",
    ["However, [contrast].",
     "Additionally, [further result of the same kind].",
     "In particular, [the specific case].",
     "Finally, [last item of the series]."],
    "Same practice as Hang's reference, where However opens its sentence and each connector has one job. Hang's reference accepts Additionally and In addition for an added point. Unfortunately is Writer C's habit and is a value word.",
    "same", ["Connectors with a clear job"],
    [q("writer_a", 131, "Additionally, we found that participants spoke more (M = 99.08, SD = 48.86) in the moderated than in the unmoderated condition (M = 77.08, SD = 47.06)."),
     q("writer_a", 189, "Finally, future work might address the case where the robot can take both task actions and social actions as both a participant and moderator of a group interaction."),
     q("writer_b", 74, "Nonetheless, a trend suggested that MO could lead to higher feelings of ostracism than AO."),
     q("writer_b", 45, "In both cases, we noted that the average inter-participant distance during the day phases of the games tended to be smaller than the average distance between the participants and the robot."),
     q("writer_c", 196, "Lastly, the Mechanical Turk study in Sec. 9.2, although compelling, illustrates simplistic datasets of human choices.")])

add("Sentence style", "Colons and semicolons", "writer_a writer_b writer_c",
    "All three use more of these marks than Hang now wants, and Hang's draft is already near the low end of their range. Colons appear {writer_a.colon}, {writer_b.colon}, and {writer_c.colon} times per 1,000 words in Writer A, Writer B, and Writer C, and {draft.colon} times in the draft. Semicolons appear {writer_a.semicolon}, {writer_b.semicolon}, and {writer_c.semicolon} times, and {draft.semicolon} times in the draft. A colon introduces a list, an explanation of the clause before it, or an example. A semicolon joins two parallel statements, and Writer A uses it most. Writer B is the most sparing with both.",
    ["[Lead-in that announces a list]: [items].",
     "One problem is [A]. The other one is [B].",
     "[Statement], since [explanation]."],
    "Hang's preference for few colons and semicolons takes priority, and nothing in the three dissertations argues against it. Readers who write with more of these marks will not find the draft heavy. Writer B's sentence with one problem and the other one is the form that Hang's reference already uses, written there as two sentences.",
    "differs", ["Few colons and semicolons", "Procedural series and enumerations"],
    [q("writer_a", 119, "When executed by a robot moderator, this serves as a multi-party extension of one-on-one socially assistive robotics: rather than a robot helping an individual achieve goals, the robot is helping a group achieve goals."),
     q("writer_a", 121, "The exact interval is task-dependent and empirically-determined; in most of the application domains in this work, it is set to between 20 and 30 seconds."),
     q("writer_b", 46, "One problem is estimating the lower-body orientation of people in a scene; the other one is detecting F-formations."),
     q("writer_c", 18, "Chapter 7 proposes that the robot should be introspective and estimate a confidence in how much to trust its representation: if the person’s behavior seems inexplicable under the robot’s current representation, then that representation must be misaligned.")])

add("Sentence style", "Parentheses for specifics", "writer_a writer_b writer_c",
    "Parentheses hold what a reader may want to check and does not need in order to follow the sentence. These are statistics, figure and section references, hypothesis labels, condition codes, and a short gloss on how something was measured. Writer C also uses them for a brief aside on the writer's expectation. The sentence still reads correctly when the parentheses are removed.",
    ["[Result] (as measured by [measure]).",
     "[Statement] (a typical example is depicted in [figure]).",
     "[Outcome] ([hypothesis label] unsupported)."],
    "Same as Hang's reference. Keep a governing condition in the sentence and out of the parentheses.",
    "same", ["Parentheses for supporting specifics"],
    [q("writer_a", 151, "The results show that the predicted trade-off did occur, but evidence of improved social features, including increased group cohesion scores and more looking around (as measured by variance in head pose), were found in the performance-reinforcing rather than performance-equalizing condition, in contrast to the predictions made in H1, H2, and H4."),
     q("writer_b", 35, "The beginning and the end of the interaction were often chaotic, because the participants were not expecting to interact with the robot and frequently got distracted with their pictures (a typical example is depicted in Fig. 5.6)."),
     q("writer_c", 68, "Further, we only tested whether users could teach features we tell them about, so we still need to test whether users can teach features they implicitly know about (as would happen when intervening to correct the robot or designing a reward from scratch).")])

add("Sentence style", "Questions", "writer_a writer_b writer_c",
    "Writer B and Writer C sometimes put the problem to the reader as a question. Question marks appear {writer_b.question} and {writer_c.question} times per 1,000 words in their chapters. The question comes at the point where the motivation turns into the approach, and the next sentence begins the answer. Writer A does not put questions to the reader. Her questions are research questions, which she lists in the introduction and states before a study, and the quoted speech of participants.",
    ["How should [agent] [action] while [condition]? One strategy is to [approach].",
     "This dissertation addresses the following research questions.",
     "Q[n]. [Research question]?"],
    "Hang's reference uses questions in headings and as research questions, which is Writer A's practice. A question in running text is not part of Hang's reference. If one is used, it opens a problem that the next sentence starts to answer.",
    "adds", ["Headings that name the question or finding", "Study actions leading to the analytical question"],
    [q("writer_a", 23, "How do participants react to a robot in the role of moderator?"),
     q("writer_a", 61, "Q2: Are children able to maintain engagement with a SAR system over time?"),
     q("writer_b", 60, "How should robots cooperate to sustain F-formations while engaged in a conversation?"),
     q("writer_b", 90, "Why can’t robots do the same and take advantage of their social environments to solve difficult perception problems?"),
     q("writer_c", 15, "What is the reason underlying these failure modes in human-robot interaction?")])

add("Sentence style", "For example after a general claim", "writer_a writer_b writer_c",
    "A general statement is followed at once by one case. Writer B opens {writer_b.open_for_example} sentences with For example, and it is her most frequent opener. Writer C uses For example and For instance ({writer_c.open_for_example} and {writer_c.open_for_instance} sentences). Writer A more often keeps the case inside the sentence with such as or for example after a comma. The example is one sentence and names the actor and what happens.",
    ["[General statement]. For example, [actor] [what happens in one case].",
     "[General statement], such as [case A] or [case B]."],
    "Same as Hang's reference, which uses For instance for a case. One example is enough for one claim.",
    "same", ["An example in a few connected sentences", "A specific case introduced by especially"],
    [q("writer_a", 23, "For example, the task-goal controller is instantiated for collaborative tasks with individual goals, with objective functions that enable the moderator to either equalize or reinforce individual performance at the task."),
     q("writer_a", 120, "In most cases, the task goals are the primary purpose of the interaction from the perspective of the participants, such as building something, solving a problem, or winning a game."),
     q("writer_b", 10, "For example, in dyadic interactions it is important that both parties are involved in the conversation, or the interaction ends."),
     q("writer_c", 131, "For example, a household robot designer may not know how an end-user would like the robot to interact with the personal possessions in the user’s home.")])

add("Sentence style", "Tense by section", "writer_a writer_b writer_c",
    "Tense follows the kind of content. An overview of a chapter is in the present (this chapter presents). A procedure that was carried out is in the past (we conducted, were recruited). A model or algorithm is described in the present (the moderator monitors). A result is in the past, and its interpretation is in the present (this suggests). A summary of a chapter and the final chapter are in the past (this chapter presented, this dissertation presented). Writer A's study discussions state findings in the present with we find that.",
    ["This chapter presents [content].",
     "[Study] was conducted with [participants].",
     "[Method] infers [quantity] from [input].",
     "[Measure] was higher in [condition], which suggests that [interpretation].",
     "This chapter presented [content]."],
    "This adds to Hang's reference, which has no pattern for tense. The scheme above is the one that all three follow. It gives a rule for a passage whose tense is in doubt, which is past for what was done in a study and for a summary, and present for what a method does and for what a result suggests.",
    "adds", ["Reporting findings and interpretations"],
    [q("writer_a", 135, "This chapter introduces the second moderation algorithm, in which the robot moderator takes actions based on the group members’ performance on a shared task."),
     q("writer_a", 133, "This chapter presented the core moderation model, in which the moderator takes social actions to affect the interaction state and improve performance relative to both task and social goals."),
     q("writer_a", 186, "This dissertation presented a model that treats moderation as a decision-making problem in which the moderator must choose social behaviors that support task goals and influence social dynamics in goal-oriented multi-party interactions."),
     q("writer_b", 27, "We conducted the experiment as a field trial during the 2013 Summer Games event at Disney Research Pittsburgh."),
     q("writer_b", 88, "We validated this idea further in the context of small group conversations."),
     q("writer_c", 67, "We introduced feature traces as a novel type of human input that allows for intuitive teaching of non-linear features from high-dimensional state spaces.")])

# --------------------------------------------------------------------------- Sentence structure

add("Sentence structure", "A result with the clause that interprets it", "writer_a writer_b writer_c",
    "A result and its interpretation are often one sentence. The result is the main clause, and a clause that begins with suggesting that, supporting, indicating, or which means carries the interpretation. Writer A uses suggesting that most often. Writer B and Writer C use it a few times, and Writer C also uses which means that. The interpretation is hedged, and the result is not.",
    ["[Result with its values], suggesting that [bounded interpretation].",
     "[Test result], supporting hypothesis H[n] ([figure]).",
     "[Observation], which means that [consequence]."],
    "This is the structure that Hang kept in the Chapter 8 review, where a result stayed together with its which suggests that clause. Hang's form is which suggests that. The three write suggesting that and do not use Hang's form, and the structure of the sentence is the same.",
    "same", ["Known information leading to new information", "One main job and varied sentence length", "Observation interpretation and explanation"],
    [q("writer_a", 132, "In the group cohesion questionnaire scores and overall participant speech we found support for two of our hypotheses, suggesting that using moderation behaviors on a robot in a multi-party interaction can improve the human-human interactions."),
     q("writer_a", 131, "A paired t-test on the group cohesion scores showed marginal significance (p = 0.06), supporting hypothesis H1 (Figure 5.4)."),
     q("writer_b", 35, "These children tended to stay on the ground for long periods (M = 74.3 seconds, SE = 11.4), suggesting that they felt comfortable in close proximity with the robot."),
     q("writer_c", 56, "In addition, participants found our teaching protocol intuitive, suggesting that feature traces can be useful for teaching features outside of the system designer’s setting.")])

add("Sentence structure", "Concession first", "writer_a writer_b writer_c",
    "A sentence grants a point and then states the main one. The granted point opens the sentence with While, Although, or Even though, and the main clause follows. All three open with While. Writer A and Writer C also use Although, and Writer B uses Even though. The pattern is common where a result is mixed, a method has a limit, or the scope is narrower than the general case.",
    ["While [what was not found], [what was found], suggesting that [interpretation].",
     "Although [general case], this dissertation focuses on [narrower case].",
     "While [method] enables [benefit], there are several limitations that [consequence]."],
    "Same as Hang's reference, which keeps the focus of the sentence in the second clause. Hang also places while after the main clause for an added contrast.",
    "same", ["Concession with while"],
    [q("writer_a", 74, "While we do not find changes in their MLU, we do find that they use more complex speech with the robot over time, suggesting that the social presence of the robot encouraged child-robot relationship building."),
     q("writer_a", 119, "Although in general a moderator might take both task-related and social actions, we focus on the case where the moderator does not directly participate in the task, but only takes social actions to affect the interaction state."),
     q("writer_b", 45, "Even though this difference was small and could have been influenced by the lack of counterbalancing, we suspect that Chester’s role could have induced this result."),
     q("writer_c", 68, "While FERL enables robots to learn features and induce structure in reward learning, there are several limitations that may affect its usability.")])

add("Sentence structure", "Rather than and instead", "writer_a writer_b writer_c",
    "The approach of the dissertation is set against the usual one inside the sentence. Rather than introduces what the work does not do, and the main clause says what it does. Writer C uses it most, and also opens sentences with Instead and By contrast. Writer B and Writer A use rather than for a design decision and for the kind of claim that the data support.",
    ["[Approach] by [what it does], rather than [the usual alternative].",
     "[Behaviors A and B] should be [treated] jointly, rather than independently of each other.",
     "Prior work [approach]. By contrast, this chapter [approach]."],
    "Same job as the literal alternative in Hang's reference, which also offers the short form with not and whereas. The usual alternative has to be one that the cited work takes.",
    "same", ["A literal alternative"],
    [q("writer_a", 97, "Consequently, data analysis takes an exploratory approach towards examining patterns in the data rather than focusing on statistical rigor."),
     q("writer_b", 2, "Our results reinforce the importance of communicative motion behavior for robots, and suggest that their body and gaze behaviors should be designed and controlled jointly, rather than independently of each other."),
     q("writer_c", 112, "By contrast, we propose that if learning generalizable representations is the goal, then we should ask the user for input that is specifically meant to teach the representation itself, rather than input meant to teach the full reward and hoping to extract a good representation along the way."),
     q("writer_c", 35, "We argue that the robot does not have to learn everything at once; instead, it can divide-and-conquer the reward learning problem and focus on explicitly learning the features separately from learning how to combine them into the reward.")])

add("Sentence structure", "First, Second, Third", "writer_a writer_b writer_c",
    "Reasons, limits, and steps are counted. Writer B announces the number (the motivation was twofold, limited in several ways) and then opens each item with First, Second, and Third. Writer C counts the reasons why an approach helps in the same way. Writer A more often uses a numbered list for algorithms and questions, and One possible direction, Another area, and Finally for a series in a paragraph.",
    ["The motivation for [change] was twofold. First, [reason]. Second, [reason].",
     "[Claim]. First, [reason]. Second, [reason]. Third, [reason].",
     "One possible direction is [A]. Another area of future work is [B]. Finally, [C]."],
    "Same as Hang's reference, which uses One is and The other one is for two items and First, Then, and Finally for a real sequence. Announcing the number is a small addition that helps a long paragraph.",
    "same", ["Procedural series and enumerations", "Connectors with a clear job"],
    [q("writer_a", 188, "Another area of future work is addressing the problem of mediation, or the case where the goals of the individual group members are in conflict."),
     q("writer_b", 37, "The motivation for these changes was twofold."),
     q("writer_b", 37, "First, we wanted to study conversations in HRI with a different group of participants that were not as impulsive as children."),
     q("writer_b", 74, "Third, the perception system that we implemented for the experiment required instrumentation."),
     q("writer_c", 68, "Second, feature traces give information about states that are not on optimal trajectories, be it states with high feature values that are undesirable, or states with low feature values where other, more important features have high values.")])

add("Sentence structure", "Purpose before the action", "writer_a writer_b writer_c",
    "A sentence that reports a step often begins with its purpose. To and In order to open the sentence, and the action follows as the main clause. All three use this for analysis steps and design decisions, so that each step is read as an answer to a need. Writer A often writes In order to, which Writer B and Writer C rarely use, and all three write To.",
    ["To [purpose], [the analysis] [action].",
     "In order to [purpose], [method] [operation] if [condition]."],
    "Same as Hang's reference. In the impersonal voice the main clause takes the analysis, the study, or a passive verb as its subject.",
    "same", ["Purpose attached to an action"],
    [q("writer_a", 122, "In order to achieve this, the moderation algorithm triggers a moderation behavior if some participant has not spoken in a 30-second window or if any one participant has spoken for more than half of the time in that window."),
     q("writer_a", 68, "To determine the level of engagement between the robot and the child during the intervention, we calculated the children’s mean response time (in seconds) when prompted by the robot’s verbal questions."),
     q("writer_b", 60, "To further our understanding of robot positioning during group conversations, we conducted another experiment where our mobile robot interacted with small groups of people."),
     q("writer_c", 35, "To provide a feature trace, the person guides the robot from states where the feature is highly expressed to states where it is not, in a monotonic fashion.")])

add("Sentence structure", "This with a noun", "writer_a writer_b writer_c",
    "The next sentence picks up the previous one with This or These and a noun that names it, such as this approach, this framework, this limitation, this validation, this dependency, or these insights. The noun classifies what was just said, which tells the reader how to take it. Writer A and Writer B rarely use This without a noun, and Writer C does so more often.",
    ["This [approach / framework] provides [what it provides].",
     "This limitation motivated [next step].",
     "This validation is important because [reason]."],
    "Hang's reference lets the next sentence take up what the previous one introduced, and accepts plain This when it refers to the statement just made. The noun is the safer choice when more than one referent is possible.",
    "same", ["Known information leading to new information"],
    [q("writer_a", 17, "This framework provides a basis for the development of a series of control algorithms for robot moderators to assist groups of people in improving task performance and managing the social dynamics of interactions in diverse domains."),
     q("writer_b", 88, "This validation is important because it sets the foundations for using spatial behavior as a mechanism to improve robot perception."),
     q("writer_b", 12, "This mutual dependency suggests that robot gaze and body motion must be designed and controlled jointly, rather than independently of each other."),
     q("writer_c", 16, "This example illustrates that if we want robots to act for and with people, their representations must not be just functional but also reflective of what humans care about, i.e. their representations must be aligned with humans’."),
     q("writer_c", 35, "To bypass this feature specification problem, state-of-the-art deep Inverse Reinforcement Learning (IRL) methods [291, 96, 50] learn rewards defined directly on the high-dimensional raw state (or observation) space, thereby implicitly constructing features automatically from task demonstrations.")])

add("Sentence structure", "Parallel sentences for conditions", "writer_a writer_b writer_c",
    "Two conditions, groups, or cases are described in sentences of the same shape. Writer B writes in the former case and in the latter. Writer A gives the two conditions the same clause structure with the outcomes exchanged. Writer C repeats an opening phrase across three sentences. The repeated shape lets the reader compare the parts that differ.",
    ["In the former case, [description]. In the latter, [description].",
     "[Condition A] improved [X] but reduced [Y], and [condition B] improved [Y] but reduced [X].",
     "Without [knowledge A], [failure A]. Without [knowledge B], [failure B]."],
    "Same as Hang's reference. Give each side of the comparison its own subject and verb, which is Hang's rule for complete clauses.",
    "same", ["Parallel sentences for a comparison", "Matched factors and endpoints", "Complete clauses in place of elliptical endings"],
    [q("writer_a", 153, "In this study, there was a negative relationship between task performance and positive social features, with the performance-reinforcing robot improving group cohesion and helpful behavior but reducing task performance, and the performance-equalizing robot improving task performance but decreasing group cohesion and helpful behavior."),
     q("writer_b", 25, "In the former case, the robot had the same role as the participants."),
     q("writer_b", 25, "In the latter, the robot acted as a leader and was more in control of the group."),
     q("writer_c", 16, "Without an understanding of personal space, the assistive robot moves the user’s cup inches away from their face [43]."),
     q("writer_c", 16, "Without knowing about jaywalking pedestrians, the autonomous car cannot properly detect them and fatally crashes into them [202].")])

add("Sentence structure", "The more, the more", "writer_a writer_b writer_c",
    "A relationship between two quantities is stated as a proportion in words. Writer B uses it for a general fact about sensing, Writer A for a measured relationship between how often the robot spoke to a participant and what the participant reported, and Writer C for the cost of a larger state space. The sentence gives the direction of the relationship, and the statistic follows when the relationship was measured.",
    ["The more [quantity A], the more [quantity B] ([statistic]).",
     "The higher [quantity A], the more [quantity B] is needed."],
    "This adds to Hang's reference. Hang's rule is to give the correlation value, so a measured relationship written this way needs its r value in the same sentence. For a general fact, a citation takes that place.",
    "adds", ["Numbers and measured comparisons", "Matched factors and endpoints"],
    [q("writer_a", 152, "We found that the more the robot spoke to participants, the higher group cohesion they reported"),
     q("writer_b", 10, "From a sensing perspective, the more people are around a robot, the more noisy and incomplete sensor data tends to be."),
     q("writer_c", 37, "The higher dimensional the state, the more human input is needed to disambiguate between those functions sufficiently to find a reward function which accurately captures human preferences")])

add("Sentence structure", "Because at the start", "writer_a writer_b writer_c",
    "A reason that governs the whole sentence is placed first. All three open sentences with Because when a design decision follows from a property of the problem or from an earlier result. Writer A uses it to justify the evaluation domain, Writer B to explain why a second protocol was designed, and Writer C to explain why a class of methods has its form. Writer C more often opens such a sentence with Since.",
    ["Because [property of the problem], [design decision].",
     "Because [earlier observation], [next study or method] was designed to [purpose]."],
    "Hang's reference uses since for a reason and keeps a governing condition attached to its claim. Because at the start of a sentence does the same job and is common in all three.",
    "same", ["Local reasons and governing conditions"],
    [q("writer_a", 20, "Because moderation is an inherently goal-directed process, the model is evaluated in the domain of socially assistive robotics (SAR)."),
     q("writer_b", 11, "Because the bystander effect emerged during this experiment, we designed another more controlled protocol to further study social conversations and spatial behavior."),
     q("writer_c", 67, "Because they have to perform updates in real time from very little input, online reward learning methods represent the reward as a linear function of a set of hand-engineered features.")])

# --------------------------------------------------------------------------- Storytelling style

add("Storytelling style", "The introduction", "writer_a writer_b writer_c",
    "The three introductions open in different ways and cover the same ground. Writer B starts from an application need, shows a scene, names the overlooked problem, states the goal, explains why the problem has structure, names the main insight, lists the challenges, limits the scope, and outlines the chapters. Writer C starts from failures of deployed systems, asks what is missing, builds one example, states her position and core insight, and walks through the parts. Writer A starts from a definition, states what the dissertation presents, explains the evaluation domain, describes the approach with a figure, and lists contributions and the outline. All three reach the statement of what the dissertation does within the first two pages.",
    ["Need → scene → gap → goal → insight → challenges → scope → outline.",
     "Failures → question → example → position → core insight → parts.",
     "Definition → what is presented → domain → approach figure → contributions → outline."],
    "Hang's Introduction has an Overview, three sections on the studies, Contributions, and an Outline, which is closest to Writer A's. Hang's reference builds the opening around an assumption about human teaching, which is the gap move in Writer B and Writer C.",
    "same", ["An introduction built around a consequential assumption"],
    [q("writer_a", 19, "In this work, moderation is defined as the process of controlling or directing a group interaction."),
     q("writer_b", 8, "The success of many robots in unstructured, human environments hinges on their ability to appropriately interact with and around people [42, 127]."),
     q("writer_b", 10, "Several challenges arise upon studying group conversations in HRI."),
     q("writer_c", 15, "Despite this rise of autonomous system integration, seamless robot interaction with people remains elusive: autonomous cars still cause crashes in unconventional situations [202], flight control systems create tug of war scenarios in spite of conflicting pilot interventions [105], and, as we will see in this thesis, personal robots move objects uncomfortably close to their users [43].")])

add("Storytelling style", "An outline with content", "writer_a writer_b writer_c",
    "The outline says what each chapter contributes. Writer A gives one sentence for each chapter with a verb that fits its content. Writer B gives a paragraph for each chapter that includes the question, the main result, and the venue. Writer C gives a paragraph for each part that explains why the part is needed and how the chapters in it differ. Inside a chapter, Writer C also lists what each section does.",
    ["[Chapter] reviews [literature] and describes [early work] that motivates [approach].",
     "([Chapter]) [Title]. [Question]. [Approach]. [Main result].",
     "[Section] frames [problem]. [Section] presents [method]. [Section] presents the results of [study]."],
    "Hang's Outline has one sentence for each chapter, which is Writer A's form. Hang's reference asks for a roadmap with actual content. Writer B's version puts the main result of each chapter in the outline, which lets a reader see the argument of the dissertation on one page.",
    "same", ["A roadmap with actual content"],
    [q("writer_a", 26, "Chapter 2 reviews related work in human-robot interaction, robot manipulation, and multi-party interaction modeling, and describes early work with children that motivates the utility of moderated group interactions with robots."),
     q("writer_b", 12, "Our results suggest that the proposed framework can help better detect non-interacting people in social environments, like bystanders, without sacrificing group detection performance."),
     q("writer_c", 17, "In this first part, we present a unifying lens on aligning robot and human representations that serves as the foundation on top of which the remaining three parts of the thesis are built."),
     q("writer_c", 132, "Sec. 7.2 frames the confidence estimation problem more formally for scenarios where the human and robot operate on the same dynamical system.")])

add("Storytelling style", "Chapter openings", "writer_a writer_b writer_c",
    "A chapter opening tells the reader what the chapter contains and where it sits. Writer A begins each chapter before the last with a short abstract in italics that says what the chapter presents and, for a study chapter, what was found. A paragraph that places the chapter after the earlier ones follows. Writer B begins with what the chapter presents or with what the previous experiments left open. Writer C begins with the publication note and a figure, then a scene, the problem with existing methods, her argument, and the contributions of the chapter.",
    ["This chapter introduces [method], in which [one clause]. [Method] is then [instantiated / evaluated] in [study]. The results show that [finding].",
     "In the [earlier studies], [what was the case]. This chapter examines [what follows from it]."],
    "Hang's study chapters open with a summary of the study and its findings, followed by where the related work is reviewed and, for the published chapters, where the work appeared. That is Writer A's opening. The summary states the finding and does not only announce the topic.",
    "same", ["A roadmap with actual content", "The three stage dissertation arc"],
    [q("writer_a", 154, "This chapter presents the third moderation algorithm, which directly models the social relationships between users as a directed graph and takes actions to affect those relationships."),
     q("writer_a", 118, "We find that participants are accepting of the robot in the moderator role and that the robot moderator is able to change the interaction."),
     q("writer_b", 60, "In the first two experiments presented in Chapter 5, the orientation of the robot was manually controlled by a wizard during the whole interaction."),
     q("writer_c", 112, "Just like in Chapter 3, we are motivated here by learning representations that lead to learning generalizable rewards.")])

add("Storytelling style", "Linking a chapter to the one before", "writer_a writer_b writer_c",
    "The first paragraphs of a chapter say what the previous chapter established and what this one adds. Writer A writes that the results presented in the previous chapter support a claim and that this chapter builds on those results. Writer B writes that a limitation or a success in the last experiment motivated the next one. Writer C writes what has been assumed so far and why that is not always enough, or that now that one thing has been tested, the next is analyzed.",
    ["The results presented in [chapter] support [claim]. This chapter builds on those results to [purpose].",
     "This limitation motivated [the work in this chapter].",
     "So far, [assumption]. [Why it does not always hold]. In [chapter], [what is done about it]."],
    "Same as the handoff in Hang's reference, and Hang's chapter connections already follow Writer A. Keep the boundary that the studies used different tasks and participants, so the link is a motivation and not a single pipeline.",
    "same", ["A study finding leading to a method", "The three stage dissertation arc"],
    [q("writer_a", 135, "The results presented in Chapter 5 support the use of a socially assistive robot moderator in group interactions and indicate that such a moderator may be able to improve the interaction, even without the use of speech understanding."),
     q("writer_a", 135, "In this chapter, we build on those results to develop an algorithm for moderation that provides task-related support to participants in the service of social goals."),
     q("writer_b", 12, "The success of the orientation behaviors that we studied in our last experiment motivated us to explore reinforcement learning techniques to generate socially appropriate orientation behaviors for robots during multi-party conversations."),
     q("writer_c", 56, "Now that we have tested our method for learning features with both experts and non-experts, we analyze how the learned features affect reward learning."),
     q("writer_c", 18, "While this chapter showcases this insight in learning from physical demonstrations or corrections, Chapter 8 applies it even more broadly to teleoperation in shared autonomy.")])

add("Storytelling style", "Chapter endings", "writer_a writer_b writer_c",
    "A chapter ends by saying what it showed and what that provides for the rest of the dissertation. Writer A ends each chapter after the introduction with a section titled Summary, written in the past tense, that restates the method, the study, and the result, and closes with what the results support. Writer B ends the long study chapter with a Summary whose last sentence points to the next chapter, and two later chapters with a Discussion. Writer C ends each chapter with a Discussion that restates the proposal and gives implications and limitations, and it often closes with a sentence that begins with Overall.",
    ["This chapter presented [content]. [Method] was [instantiated / evaluated] in [study]. [Result]. These results support [claim] and provide a basis for [next step].",
     "The next chapter describes [what follows]."],
    "Hang's study chapters end with a Discussion and a Summary, which is Writer A's structure. Hang's reference says to end with a link to the next chapter only when that chapter addresses the named question.",
    "same", ["Discussion synthesis and its boundary"],
    [q("writer_a", 117, "This chapter presented four studies of human-robot interaction that inform the development of the robot controllers used in this dissertation."),
     q("writer_a", 153, "These results demonstrate that task-related moderation can affect social factors, and show that the moderator can improve social features of the interaction even when participants report not paying close attention to the robot’s behavior."),
     q("writer_b", 45, "The next chapter describes our efforts in this direction."),
     q("writer_c", 67, "In this work, we propose that robots can learn more generalizable rewards by using a divide-and-conquer approach, focusing on learning features separately from learning how to combine them."),
     q("writer_c", 126, "They improve upon the state of the art, and can benefit from further exploration in how to combine them with other inputs and self-supervision, and how to make them easier through better interfaces and query selection algorithms.")])

add("Storytelling style", "A study in a fixed order", "writer_a writer_b writer_c",
    "Every study is reported in the same order, so a reader can find the same information in the same place. Writer A uses Methodology, Results, and Discussion, with research questions or hypotheses first, then design, setup, measures, and participants, and results grouped by measure. Writer B uses Method, Results, and Discussion with Participants and Procedure as subsections. Writer C uses run-in labels in a fixed sequence, which are Manipulated Variables, Dependent Measures, Hypotheses, and Participants, followed by an analysis divided into objective and subjective results and a short Summary.",
    ["The study addressed [N] research questions, as follows.",
     "Participants. [N, recruitment, sample properties]. Hypotheses. H[n]. [Statement].",
     "This section presents the results of [study] according to the measures described in [section]."],
    "Hang's study chapters all end with a Discussion and a Summary. The sections before them have different names in different chapters, such as Study Design and Experimental Setup in one and Methodology in others. Each of the three keeps one order and one set of headings for every study. Whether to align the headings is Hang's decision. Hang's reference handles each results paragraph.",
    "same", ["A results paragraph answering one comparison", "Study actions leading to the analytical question"],
    [q("writer_a", 61, "Our study addressed five research questions, as follows:"),
     q("writer_a", 130, "This section presents the results of the validation study according to the measures described in Section 5.3.1.5."),
     q("writer_b", 27, "Participants only experienced one of two conditions: without sidekick (C) or sidekick (S)."),
     q("writer_c", 54, "Hypotheses. H4: FERL learns good features from non-expert user data."),
     q("writer_c", 56, "Both the objective and subjective results provide evidence that non-expert users can teach the robot reasonable features using our FERL protocol.")])

add("Storytelling style", "A method from idea to steps", "writer_a writer_b writer_c",
    "A method is explained in words before it is given in symbols or as an algorithm. Writer A describes the model as a cycle of monitoring, evaluating, and acting, defines its terms, and only then gives the algorithm and one instantiation. Writer B states the problem and its assumptions, gives the core of the framework in one sentence, and walks through the steps with First and Then. Writer C gives the intuition, says why the direct approach is difficult, and then says what is done instead.",
    ["At the core of [framework] is [procedure]. First, [step]. Then, [step].",
     "Since [direct approach] is difficult, [method] instead [operation].",
     "Throughout [process], [agent] [monitors / computes] [quantity], taking [action] at [interval or condition]."],
    "Same as Hang's reference, which explains the meaning of a signal and the intuition before notation and losses. A method name is the subject of its own operations.",
    "same", ["Teaching a method from meaning to evaluation", "Explaining the mechanism", "An intuition leading to an operation"],
    [q("writer_a", 121, "Throughout the interaction, the moderator monitors the state, taking actions intended to serve the goals of the interaction at regular intervals."),
     q("writer_b", 48, "At the core of the framework is an alternating optimization procedure that we named GrupO, for Group detection and Orientation tracking."),
     q("writer_b", 48, "First, GrupO estimates likely conversations by finding F-formations."),
     q("writer_c", 114, "Our intuition is that if a human judges two behaviors to be similar, then their representations should also be similar."),
     q("writer_c", 114, "Since directly asking if two trajectories are similar is difficult without an explicit threshold, we instead present the human with a triplet of trajectories and ask them to pick the two most similar (or, equivalently, the most dissimilar one).")])

add("Storytelling style", "Related work that ends on this work", "writer_a writer_b writer_c",
    "A passage of related work closes by placing the dissertation next to what was just reviewed. Writer A says what the dissertation leverages from a field and what it contributes to it, and how her robot differs from similar ones. Writer B ends a group of studies with what remains unclear and with our efforts build upon this work. Writer C ends each group with By contrast or We instead and the specific difference. The three place related work differently. Writer A has one background chapter, Writer B has a background chapter, a related work chapter, and short sections before each experiment, and Writer C has a Prior Work section in each chapter.",
    ["This dissertation leverages results in [field] about [topic], and contributes to this area by [contribution].",
     "It is unclear from this work whether [open question].",
     "Prior work [approach]. This chapter instead [approach], rather than [alternative]."],
    "Same as Hang's reference. Hang's structure is Writer A's, with one Background chapter that each study chapter points to. A difference is not by itself an advantage.",
    "same", ["Related work ending with the specific difference", "Prior work and research gaps"],
    [q("writer_a", 29, "This dissertation leverages results in CSCW about group interactions, and contributes to this area by increasing our understanding of agents in multi-party interactions."),
     q("writer_a", 46, "Our design occupies a similar niche, but was developed specifically for SAR research with more degrees of freedom in the body than Maki, Keepon, Travis, DragonBot, and Jibo and more degrees of freedom in the animated face than Keepon, iCat, and Maki."),
     q("writer_b", 26, "There are logical reasons for different proxemics when robots are independent, but it is unclear from this work whether co-location, such as in the case of Chester and Blink, impacts proxemics."),
     q("writer_b", 26, "Our efforts are inspired by these prior works."),
     q("writer_c", 114, "We instead focus on fully learning a lower-dimensional feature representation all-at-once, rather than one at a time.")])

add("Storytelling style", "A discussion in themed paragraphs", "writer_a writer_b writer_c",
    "A discussion is divided by theme, and each theme is visible at the start of its paragraph. Writer A uses a run-in heading that ends with a colon. Writer B uses a lead sentence in small capitals. Writer C uses a run-in heading that ends with a period, such as Implications for a setting and Limitations and Future Work. The themes cover what was found, what it means for design, what limits it, and what comes next.",
    ["[Theme as a noun phrase]. [Paragraph].",
     "[Finding as a short sentence]. [Paragraph with the evidence].",
     "Limitations and Future Work. [Paragraph]."],
    "Same as Hang's reference, which gives discussion run-in headings a concrete subject. Writer A's headings end with a colon. A period after the heading, as in Writer C, follows Hang's preference for fewer colons.",
    "same", ["Headings that name the question or finding", "Discussion synthesis and its boundary"],
    [q("writer_a", 112, "Between-Group Differences: The groups participating in this study varied in personality, gender composition, and age, but all indicated a high degree of group cohesion after interacting with the robot."),
     q("writer_a", 113, "Towards Moderators in Intergenerational Groups: This pilot study demonstrated that the audience exists for SAR systems that serve as in-home companions and support intergenerational family interactions."),
     q("writer_b", 35, "There were no differences for spatial behavior between conditions."),
     q("writer_c", 67, "Implications for Online Reward Learning."),
     q("writer_c", 67, "Implications for Learning Complex Rewards from Demonstrations.")])

add("Storytelling style", "Discussion order", "writer_a writer_b writer_c",
    "A study discussion begins by restating the goal or what was done, in one or two sentences. It then reports which hypotheses were supported, explains the results that went against expectation, states the limits of the study, and ends with what the study provides for the following work. Writer A and Writer B follow this order closely. Writer C begins with the proposal and the main evidence and then gives implications before limitations.",
    ["The goal of this study was to examine [question].",
     "[What was done, in one sentence]. [What was found]. [What was not found, with a possible reason]. [Limits]. [What this provides for the next chapter].",
     "The results of this study motivate [subsequent work]."],
    "Same as the discussion pattern in Hang's reference, which moves from connection to evidence, implication, boundary, and next question. A study discussion in the three ends by linking forward, and Hang's rule allows that link when the next chapter addresses the question.",
    "same", ["Discussion synthesis and its boundary"],
    [q("writer_a", 73, "The goal of this study was to examine the feasibility of a SAR-based intervention for teaching children about nutrition."),
     q("writer_a", 99, "The insights from this work informed the structure of child-robot interactions with children with autism, the focus of the fourth validation study included in this dissertation work, described in Section 8.2."),
     q("writer_b", 87, "We explored reinforcement learning methods to control the orientation of a robot during simulated multi-party conversations."),
     q("writer_b", 74, "The experiment described in this chapter was limited in several ways"),
     q("writer_c", 196, "We propose a new probabilistic human behavior model and present compelling evidence that it better captures human decision making and it attenuates inference errors that arise due to similar selections, increasing accuracy and robustness.")])

add("Storytelling style", "Future work from scope and limits", "writer_a writer_b writer_c",
    "Future work is derived from the choices and limits of the dissertation. Writer A says that a number of choices were made in scoping the work and that each choice provides a starting point, and then takes the choices one at a time. Writer B titles the section Limitations and Avenues for Future Research and pairs each limitation with an avenue. Writer C says that the dissertation has made progress and that it opens further directions, and groups them under three headings. Each direction starts from what the dissertation did and says what would change.",
    ["A number of choices were made in scoping this dissertation, and each provides a starting point for future work.",
     "So far, [what the dissertation did]. Moving forward, [direction] could [what it would make possible].",
     "[What is not addressed in this dissertation]. Future research might [action] in order to [purpose]."],
    "This is the structure of Hang's future work, which starts from the dissertation and moves to the planned step. Hang's rule for these paragraphs still applies, so each one ends on the planned step or the mechanism and takes its content from Hang's notes.",
    "same", ["Future work drafted from notes", "Limitations and future work"],
    [q("writer_a", 188, "A number of choices were made in scoping the work presented in this dissertation; each of these choices provides a starting point for future development of robot moderators."),
     q("writer_b", 89, "While our work showed the benefits of enabling robots to reason about F-formations, it is by no means without limitations."),
     q("writer_b", 89, "So far, our efforts have focused on building model-based approaches to enable robots to reason about human spatial behavior typical of group conversations."),
     q("writer_c", 198, "This thesis has made progress in enabling robots to learn human-aligned representations with explicit representation-specific feedback, but it opens the door to more alternative research directions in this space.")])

add("Storytelling style", "The final chapter", "writer_a writer_b writer_c",
    "The final chapters are short, at three to four pages each. Writer A's is titled Summary and has a recap paragraph, the contributions in the past tense, the future directions, and a closing paragraph on the ethical concern of the field. Writer B's is titled Conclusion and has two take-home messages, a list of contributions, and limitations with avenues for future research. Writer C's is titled Conclusion and Future Work and has a recap of her position, the limitation that leads to a broader question, and three groups of directions. None of the three has a separate chapter that discusses the findings across chapters.",
    ["This dissertation presented [object] that [what it does]. [What the studies showed, in one sentence].",
     "The main take-home messages of this dissertation are [two or three numbered statements]."],
    "Hang's dissertation has an Overall Discussion chapter before the Conclusion, which goes beyond what the three did and is Hang's own structure. With that chapter in place, the Conclusion can stay as short as theirs. Writer B's take-home messages are a form that fits a summary of contributions.",
    "adds", ["Discussion synthesis and its boundary", "Contribution statements"],
    [q("writer_a", 186, "These studies showed that participants were accepting of the robot in the moderator role, and that a robot moderator could support positive features of human-human interaction such as helpfulness and group cohesion."),
     q("writer_b", 88, "F-formations naturally emerge in HRI."),
     q("writer_b", 88, "Reasoning about F-formations is useful for robots."),
     q("writer_c", 197, "In this thesis, we approached interaction by explicitly tackling representation alignment, rather than hoping it will naturally emerge."),
     q("writer_c", 197, "However, the core of this work had the human in the teacher role feeding the robot data about their representation.")])


# One line for the comparison with Hang's reference, for the patterns that add
# to it or differ from it.
BRIEF = {
    "Scope statements": "One or two sentences on what the dissertation does not cover.",
    "Pointing to figures, sections, and chapters": "One figure in the introduction that shows the whole approach, and plain wording for references.",
    "One example carried through": "A single example reused inside a chapter.",
    "The thesis in one sentence": "One sentence for the thesis, repeated in the same words.",
    "Candor about costs": "A plain statement of what a method cost or did not solve.",
    "Ending on the wider stake": "A short closing on what the work is for.",
    "Questions": "Research questions as a list, and an occasional question in running text.",
    "Tense by section": "A rule for tense by kind of content.",
    "The more, the more": "A relationship between two quantities stated as a proportion.",
    "The final chapter": "A short final chapter, with take-home messages as an option.",
    "Evaluative and emphatic words": "Writer C uses strong evaluative words. Hang's reference asks for few value words.",
    "First person and the impersonal voice": "All three use we, and Writer A uses it least. Hang's dissertation is impersonal.",
    "Register": "Writer C uses contractions and idioms. Hang's reference asks for literal wording.",
    "Colons and semicolons": "All three use more of both marks than Hang wants. Hang's draft is already near the low end.",
}
