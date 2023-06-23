from experta import *

class JobType(Fact):
    pass

# Frontend Facts

class PerfetHtmlCss(Fact):
    pass
class GoodBootstrab(Fact):
    pass
class ProfessionalCss(Fact):
    pass
class GoodJsAndFram(Fact):
    pass
class GoodJsOnly(Fact):
    pass
class GoodSolveProblem(Fact):
    pass
class GoodGit(Fact):
    pass
class GoodSeo(Fact):
    pass
class FrameworkType(Fact):
    pass
class AngularQ(Fact):
    pass
class GoodTypeScript(Fact):
    pass
class UnderstandingBrowser(Fact):
    pass
class GoodEngDoc(Fact):
    pass
class ReactQ(Fact):
    pass
class VueQ(Fact):
    pass

# AI Facts ################################################################################
class Graduated(Fact):
    pass
class GoodAlgorithms(Fact):
    pass
class GoodPythonLang(Fact):
    pass
class UsingLibraries(Fact):
    pass


# Backend Facts ###########################################################################
class GoodProbblemStrDB(Fact):
    pass
class MakeSolution(Fact):
    pass
class GoodOOP(Fact):
    pass
class KnowHTMLCSSJS(Fact):
    pass
class WichLanguageUsed(Fact):
    pass
class PhpQ(Fact):
    pass
class NodeQ(Fact):
    pass
class CQ(Fact):
    pass
class LaravelQ(Fact):
    pass
class YiiQ(Fact):
    pass
class CodeigniterQ(Fact):
    pass

# UI UX Facts
class Level(Fact):
    pass
class Designs(Fact):
    pass
class Exp(Fact):
    pass
class Prototype(Fact):
    pass
class StyleG(Fact):
    pass
class Component(Fact):
    pass
class Dashboard(Fact):
    pass
class collabration(Fact):
    pass
class Khtmlcss(Fact):
    pass
class Designpattren(Fact):
    pass
class Uxproblem(Fact):
    pass
class Template(Fact):
    pass
class Graphic(Fact):
    pass
class FourProject(Fact):
    pass
class Englishcomm(Fact):
    pass
class Photoshop(Fact):
    pass
class Arch(Fact):
    pass
class Platform(Fact):
    pass
class MangeTeam(Fact):
    pass


###############################################################################################
class CodersJobs(KnowledgeEngine):
    @Rule(NOT(JobType(W())))
    def jobTypeQues(self):
        self.declare(JobType(input('Please Enter What is Your Job Type ? (frontend / backend / ai / ui ux )..')))

    @Rule(JobType('value'<<W()))
    def jobTypeValue(self,value):
        if value == 'frontend':
            self.declare(PerfetHtmlCss(input('Are You Perfect At Html and Css ? (yes/no)..')))
        elif value == 'backend':
                self.declare(GoodProbblemStrDB(input('are you good at problem solving and have a good knoladege with data stracture and good with relational or unrelational database? (yes/no)..')))
        elif value == 'ai':
            self.declare(Graduated(input('Do You Have Bachelor Degree in Computer, Or Science, Artificial Intelligence ? So Did You Graduated ? (yes/no)..')))
        elif value == 'ui ux':
            self.declare(Level(input('Which level you are Mid level OR  Senior ')))
        else:
            print('Not a Clear Answer !..')

    # UI UX Rules
    @Rule(Level('value' << W()))
    def checklevel(self, value):
        if value == 'mid level':
            self.declare(Designs(input('pro with Design system? (yes/no)..')))
        elif value == 'senior':
            self.declare(Exp(input('+ 3 years experience in UIUX (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Designs('value' << W()))
    def checkDesign(self, value):
        if value == 'no':
            self.declare(Prototype(input('good at userflow and Prototype? (yes/no)..')))
        elif value == 'yes':
            self.declare(StyleG(input('can make style guides? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Prototype('value' << W()))
    def checkprototype(self, value):
        if value == 'no':
            self.declare(Component(input('good at wireframe and design mockupand very good complex component (yes/no)..')))
        elif value == 'yes':
            self.declare(Dashboard(input('Pro with complex UI element and design dashboard? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Component('value' << W()))
    def chechIfProffesional(self, value):
        if value == 'no':
            print('You Must Take Courses !..')
        elif value == 'yes':
            print('go to Tradinos company !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(Dashboard('value' << W()))
    def checkdash(self, value):
        if value == 'no':
            print('go to Tradinos company !..')
        elif value == 'yes':
            print('go Smart soft LLC !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(StyleG('value' << W()))
    def checkStyleG(self, value):
        if value == 'no':
            self.declare(collabration(input('Collabrating with product mangeand team lead? (yes/no)..')))
        elif value == 'yes':
            self.declare(Khtmlcss(input('Good at html/css? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(collabration('value' << W()))
    def checkcoll(self, value):
        if value == 'no':
            print('Go to madfox !..')
        elif value == 'yes':
            print('Go to madfox !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(Khtmlcss('value' << W()))
    def checkHtmlcss(self, value):
        if value == 'no':
            print('Go to R-link !..')
        elif value == 'yes':
            self.declare(Designpattren(input('good with design pattren and attractive User interface (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Designpattren('value' << W()))
    def checkdesignpatren(self, value):
        if value == 'no':
            print('Go to east med !..')
        elif value == 'yes':
            self.declare(Uxproblem(input('Identifeing and trubleshoting UX problem? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Uxproblem('value' << W()))
    def checkuxproblem(self, value):
        if value == 'no':
            print('Go to east med !..')
        elif value == 'yes':
            print('Go to Gaia company !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(Exp('value' << W()))
    def checkexpirence(self, value):
        if value == 'no':
            self.declare(Template(input('Designing Templates UI assets , personas , design mockups , userflowand +1 years in UIUX (yes/no)..')))
        elif value == 'yes':
            self.declare(Graphic(input('Creating orginal Graphic designs(image and tables) (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Template('value' << W()))
    def checkassets(self, value):
        if value == 'no':
            print('XXX  !..')
        elif value == 'yes':
            self.declare(FourProject(input('Work on perfect project at least 4 real project) (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(FourProject('value' << W()))
    def checkfourproject(self, value):
        if value == 'no':
            print('XXX  !..')
        elif value == 'yes':
            self.declare(Englishcomm(input('Good english and communication (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Englishcomm('value' << W()))
    def checkenglish(self, value):
        if value == 'no':
            print('Goto PDA OR Tradios OR ZCoderZ OR Kasroad  !..')
        elif value == 'yes':
            print('Goto PDA OR Tradios OR ZCoderZ OR Kasroad  !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(Graphic('value' << W()))
    def checkgraphic(self, value):
        if value == 'no':
            self.declare(Photoshop(input('good at photoshop and illustrator and after effect (yes/no)..')))
        elif value == 'yes':
            self.declare(Arch(input('Formulating information architective and navigntion for complex datastructre (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Photoshop('value' << W()))
    def checkphotoshop(self, value):
        if value == 'no':
            print('XXX !..')
        elif value == 'yes':
            print('Goto BH-Agency  !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(Arch('value' << W()))
    def checkarch(self, value):
        if value == 'no':
            self.declare(Platform(input('great design for android , ios ,web ,and other platform  (yes/no)..')))
        elif value == 'yes':
            self.declare(MangeTeam(input('manage team of junior UX design  (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(Platform('value' << W()))
    def checkplatform(self, value):
        if value == 'no':
            print('L-oneSystem LLC ')
        elif value == 'yes':
            print(' Goto  Maids.cc OR  kaizen ')
        else:
            print('Not a Clear Answer !..')

    @Rule(MangeTeam('value' << W()))
    def checkmangeteam(self, value):
        if value == 'no':
            print('Goto  Maids.cc. OR   PDA(Princetect Digital Agency)  ')
        elif value == 'yes':
            print('Goto  Maids.cc. OR   PDA(Princetect Digital Agency)  ')
        else:
            print('Not a Clear Answer !..')



    # Frontend Rules #####################################################################################################

    @Rule(PerfetHtmlCss('value'<<W()))
    def checkIfPerfect(self,value):
        if value == 'no':
            print('You Must Take Courses !..')
        elif value == 'yes':
            self.declare(GoodBootstrab(input('Are You Good At Bootstrab [TailwindCss Optional] ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodBootstrab('value'<<W()))
    def checkIfGoodBootsrab(self,value):
        if value == 'no':
            self.declare(ProfessionalCss(input('Are You Professional At Css :[grid, complex component, animation, sass(scss)] ? (yes/no)..')))
        elif value == 'yes':
            self.declare(GoodJsAndFram(input('Are You Good At JavaScript and Know About Framework ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(ProfessionalCss('value'<<W()))
    def chechIfProffesional(self,value):
        if value == 'no':
            print('You Must Take Courses !..')
        elif value == 'yes':
            self.declare(GoodJsOnly(input('Are You Good At JavaScript ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodJsOnly('value'<<W()))
    def checkIfGoodJsOnly(self,value):
        if value == 'no':
            print('You Must Take Courses !..')
        elif value == 'yes':
            print('Intership at Madarat Idea Solution')
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodJsAndFram('value'<<W()))
    def checkIfGoodJsAndFram(self,value):
        if value == 'no':
            print('Intership at Madarat Idea Solution')
        elif value == 'yes':
            self.declare(GoodSolveProblem(input('Are You Good At Problem Solving ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodSolveProblem('value'<<W()))
    def checkIfGoodSolveProb(self,value):
        if value == 'no':
            print('Intership at Transtek Company')
        elif value == 'yes':
            self.declare(GoodGit(input('Are You Good At (Githup/Gitlap) ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodGit('value' << W()))
    def checkIfGoodGit(self, value):
        if value == 'no':
            print('Intership at Transtek Company')
        elif value == 'yes':
            self.declare(GoodSeo(input('Are You Have Good Knowledge At SEO And Build At Least 2 Projects ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodSeo('value' << W()))
    def checkIfGoodSeo(self, value):
        if value == 'no':
            print('Intership at Expentech Solution')
        elif value == 'yes':
            self.declare(FrameworkType(input('Which Framework You Used ? ( react / vue.js / angular.js )..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(FrameworkType('value' << W()))
    def frameworkType(self, value):
        if value == 'react':
            self.declare(ReactQ(input('Are You Rendering List With React? Working With JSX? Start React Components? Debugging React App? Hook? Reducs ? (yes/no)..')))
        elif value == 'vue.js':
            self.declare(VueQ(input('Do You Know Vue LCI, Vue Vite, Vue State Management, Vue Routes, API, Vue Animation, Pips & Directives, Firebase, Testing ? (yes/no)..')))
        elif value == 'angular.js':
            self.declare(AngularQ(input('Do You Know Components, Pipe, Event, Observables, Route & Routing, Firebase ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(AngularQ('value' << W()))
    def checkIfKnowAngular(self, value):
        if value == 'no':
            print('Go To BMY Company')
        elif value == 'yes':
            self.declare(GoodTypeScript(input('Are You Good At TypeScript ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodTypeScript('value' << W()))
    def checkIfGoodTS(self, value):
        if value == 'no':
            print('Go To IXCoders')
        elif value == 'yes':
            self.declare(UnderstandingBrowser(input('Are You Understanding Very Well How Browser Work & Good At Testing & Debugging? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(UnderstandingBrowser('value' << W()))
    def checkIfUnderstand(self, value):
        if value == 'no':
            print('Go To IXCoders')
        elif value == 'yes':
            self.declare(GoodEngDoc(input('Are You Good At English & Docker? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodEngDoc('value' << W()))
    def checkIfGoodEngDoc(self, value):
        if value == 'no':
            print('Learn Docker & AWS & Work Freelance')
        elif value == 'yes':
            print('Work Freelances')
        else:
            print('Not a Clear Answer !..')

    @Rule(ReactQ('value' << W()))
    def checkIfKnowReact(self, value):
        if value == 'no':
            print('Go To Websitak')
        elif value == 'yes':
            self.declare(GoodTypeScript(input('Are You Good At TypeScript ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodTypeScript('value' << W()))
    def checkIfGoodTS(self, value):
        if value == 'no':
            print('Go To Kaizen OR Kasroad OR MADFOX')
        elif value == 'yes':
            self.declare(UnderstandingBrowser(input('Are You Understanding Very Well How Browser Work & Good At Testing & Debugging? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(UnderstandingBrowser('value' << W()))
    def checkIfUnderstand(self, value):
        if value == 'no':
            print('Go To IXCoders OR Kasroad OR ALphaApps')
        elif value == 'yes':
            self.declare(GoodEngDoc(input('Are You Good At English & Docker? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodEngDoc('value' << W()))
    def checkIfGoodEngDoc(self, value):
        if value == 'no':
            print('Learn Docker & AWS & Work As Freelances')
        elif value == 'yes':
            print('Work Freelance')
        else:
            print('Not a Clear Answer !..')

    @Rule(VueQ('value' << W()))
    def checkIfKnowVue(self, value):
        if value == 'no':
            print('Go To Websitak')
        elif value == 'yes':
            self.declare(GoodTypeScript(input('Are You Good At TypeScript ? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodTypeScript('value' << W()))
    def checkIfGoodTS(self, value):
        if value == 'no':
            print('Go To ELCODE OR R-Link')
        elif value == 'yes':
            self.declare(UnderstandingBrowser(input('Are You Understanding Very Well How Browser Work & Good At Testing & Debugging? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodEngDoc('value' << W()))
    def checkIfGoodEngDoc(self, value):
        if value == 'no':
            print('Go To ELCODE')
        elif value == 'yes':
            print('Work Freelance')
        else:
            print('Not a Clear Answer !..')


# AI Rules  ##################################################################################################################

    @Rule(Graduated('value' << W()))
    def checkIfGraduated(self, value):
        if value == 'no':
            print('You Must Graduate First')
        elif value == 'yes':
            self.declare(GoodAlgorithms(input('Do You Have Good Knowledge With Machine Learning Algorithms & Deep Learning & Neural Neture? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodAlgorithms('value' << W()))
    def checkIfgoodAlgorithm(self, value):
        if value == 'no':
            print('Sorry!! No Work You Must Learn First')
        elif value == 'yes':
            self.declare(GoodPythonLang(input('Do You Have Projects With Python & Good At Algorithm & Mathmatical? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodPythonLang('value' << W()))
    def checkIfgoodpython(self, value):
        if value == 'no':
            print('Sorry!! No Work You Must Learn First')
        elif value == 'yes':
            self.declare(UsingLibraries(input('Do You Using This Libraries (scipy, scirk, itlearn, kevas, kpytorch, tensorflow)? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(UsingLibraries('value' << W()))
    def checkIfgoodLibraries(self, value):
        if value == 'no':
            print('Sorry!! No Work You Must Learn First')
        elif value == 'yes':
            print('Teacher At New horizon OR Work At Midicus')
        else:
            print('Not a Clear Answer !..')

# Backend Rules  ###########################################################################################################

    @Rule(GoodProbblemStrDB('value'<<W()))
    def checkDBPS(self,value):
        if value == 'no':
            print('backend is not your side my friend !..')
        elif value == 'yes':
            self.declare(MakeSolution(input('you will transform into solution and developing technical solution will you? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(MakeSolution('value' << W()))
    def checkSolution(self, value):
        if value == 'no':
            self.declare(
                GoodOOP(input('good at oop? and algorithm(not must)? (yes/no)..')))
        elif value == 'yes':
            self.declare(
                GoodOOP(input('good at oop? and algorithm(not must)? (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(GoodOOP('value' << W()))
    def checkOOP(self, value):
        if value == 'no':
            print('backend is not your side my friend !..')
        elif value == 'yes':
            self.declare(
                KnowHTMLCSSJS(input('familiar with HTML,CSS,JAVASCRIPT (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(KnowHTMLCSSJS('value' << W()))
    def checkHTMLCSSJS(self, value):
        if value == 'no':
            self.declare(
                WichLanguageUsed(input('which language you code with  PHP? C#? NODE.JS? ')))
        elif value == 'yes':
            self.declare(
                WichLanguageUsed(input('which language you code with  PHP? C#? NODE.JS? ')))
        else:
            print('Not a Clear Answer !..')

    @Rule(WichLanguageUsed('value' << W()))
    def checkLanguage(self, value):
        if value == 'php':
            self.declare(PhpQ(input(
                'wich framework you used?  laravel? CodeIgnitor? Yii?')))
        elif value == 'c#':
            self.declare(CQ(
                input('pro with asp.net and .net core (yes/no)..')))
        elif value == 'node.js':
            self.declare(NodeQ(
                input('good at express and very good at mongodb?  (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(PhpQ('value' << W()))
    def checkphpframew(self, value):
        if value == 'laravel':
            self.declare(LaravelQ(input(
                '+2 years experiements using laravel framework (yes/no)..')))
        elif value == 'codeigniter':
            self.declare(CodeigniterQ(
                input('+2 years experiements using codeignitor framework (yes/no)..')))
        elif value == 'node.js':
            self.declare(YiiQ(
                input('can buid aoi and good with RESTFUL api?and can fix bugs?  (yes/no)..')))
        else:
            print('Not a Clear Answer !..')

    @Rule(LaravelQ('value' << W()))
    def checklaravel(self, value):
        if value == 'no':
            print('Go to ZCoderZ   OR  IXCoders  OR  MADFOX  OR  Tradinos  OR  ALphaApps !..')
        elif value == 'yes':
            print('Go to ZCoderZ   OR  IXCoders  OR  MADFOX  OR  Tradinos  OR  ALphaApps !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(YiiQ('value' << W()))
    def chechYii(self, value):
        if value == 'no':
            print('Go MADFOX  !..')
        elif value == 'yes':
            print('Go MADFOX  !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(CodeigniterQ('value' << W()))
    def checkcodeig(self, value):
        if value == 'no':
            print('IXCoders !..')
        elif value == 'yes':
            print('IXCoders !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(CQ('value' << W()))
    def checkC(self, value):
        if value == 'no':
            print('intership/work ELCODE  OR  MADARAT OR  idea solution !..')
        elif value == 'yes':
            print('intership/work ELCODE  OR  MADARAT OR  idea solution !..')
        else:
            print('Not a Clear Answer !..')

    @Rule(NodeQ('value' << W()))
    def checknode(self, value):
        if value == 'no':
            print('ZCoderZ  OR  R-link OR  sardeh Tech !..')
        elif value == 'yes':
            print(' Masoudi ST OR IXCoders OR ALphaApps!..')
        else:
            print('Not a Clear Answer !..')


x=CodersJobs()
x.reset()
x.run()