/**************************** 
 * Configural_Featural Test *
 ****************************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'configural_featural';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'design': '1', 'position': '2'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(screen_scaleRoutineBegin());
flowScheduler.add(screen_scaleRoutineEachFrame());
flowScheduler.add(screen_scaleRoutineEnd());
flowScheduler.add(prac_instructionsRoutineBegin());
flowScheduler.add(prac_instructionsRoutineEachFrame());
flowScheduler.add(prac_instructionsRoutineEnd());
const pTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pTrialsLoopBegin, pTrialsLoopScheduler);
flowScheduler.add(pTrialsLoopScheduler);
flowScheduler.add(pTrialsLoopEnd);
flowScheduler.add(startInstructRoutineBegin());
flowScheduler.add(startInstructRoutineEachFrame());
flowScheduler.add(startInstructRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'bankcard.png', 'path': 'bankcard.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var screen_scaleClock;
var thisExp;
var win;
var event;
var shuffle;
var webbrowser;
var random;
var randint;
var round;
var oldt;
var x_size;
var y_size;
var screen_height;
var x_scale;
var y_scale;
var dbase;
var unittext;
var vsize;
var height;
var width;
var text_top;
var text_bottom;
var ccimage;
var prac_instructionsClock;
var pracCorr;
var corrFix;
var pTrial;
var pfix_color_options;
var paths;
var samepTrials;
var diffpTrials;
var sameCount;
var diffCount;
var ptrial_order;
var corrpFix;
var numPTrials;
var pfix_switch;
var prac_targetClock;
var text_6;
var image;
var prac_probeClock;
var text_7;
var image_2;
var prac_resp;
var prac_fix_resp;
var prac_feedbackClock;
var image_3;
var startInstructClock;
var fix_color_options;
var design_file;
var text_3;
var key_resp_7;
var instrBlockClock;
var instructions_image;
var key_resp_2;
var target_imgClock;
var text_4;
var target_image;
var key_resp_3;
var ISI_fixClock;
var text;
var key_resp_4;
var probe_imgClock;
var text_5;
var probe_image;
var key_resp_5;
var trial_respClock;
var text_2;
var key_resp;
var key_resp_6;
var feedbackClock;
var good_job;
var key_resp_8;
var EndScreenClock;
var allDone;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "screen_scale"
  screen_scaleClock = new util.Clock();
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  Array.prototype.append = [].push;
  shuffle = util.shuffle;
  webbrowser=window;
  
  random=Math.random;
  randint=function(min, maxplusone) {
      return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  round = function(num, n=0) {    
      return +(Math.round(num + ("e+" + n))  + ("e-" + n));
  }
  
  function shuffle_array(array) {
      for (let i = array.length - 1; i > 0; i--) {
          let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i
  
              // swap elements array[i] and array[j]
              // we use "destructuring assignment" syntax to achieve that
              // you'll find more details about that syntax in later chapters
              // same can be written as:
              // let t = array[i]; array[i] = array[j]; array[j] = t
          [array[i], array[j]] = [array[j], array[i]];
      }
      return array
  }
  console.log(shuffle_array([1,2,3,3]))
  
  function divide_subPoint1(array, divisor) {
      let array_divided = array.map(function(element) {
          return element/divisor - 0.1;
      });
      return array_divided
  }
  
  function round_array(array) {
      array = array.map(function(each_element){
          return Math.round(each_element);
      }); 
      return array
  }
  
  psychoJS.downloadResources([{name: ("Stimuli/greenCheck.png"), path:("Stimuli/greenCheck.png")},
  {name: ("Stimuli/redWrong.png"), path:("Stimuli/redWrong.png")},
  {name: ("Stimuli/edmd.png"), path:("Stimuli/edmd.png")},
  {name: ("Stimuli/eimd.png"), path:("Stimuli/eimd.png")},
  {name: ("Stimuli/eomu.png"), path:("Stimuli/eomu.png")},
  {name: ("Stimuli/eumu.png"), path:("Stimuli/eumu.png")},
  {name: ("Stimuli/f15.png"), path:("Stimuli/f15.png")},
  {name: ("Stimuli/f24.png"), path:("Stimuli/f24.png")},
  {name: ("Stimuli/f131.png"), path:("Stimuli/f131.png")},
  {name: ("Stimuli/f142.png"), path:("Stimuli/f142.png")},
  {name: ("Stimuli/H-8sim0.png"), path:("Stimuli/H-8sim0.png")},
  {name: ("Stimuli/H-8sim1.png"), path:("Stimuli/H-8sim1.png")},
  {name: ("Stimuli/H-8sim2.png"), path:("Stimuli/H-8sim2.png")},
  {name: ("Stimuli/H-8sim3.png"), path:("Stimuli/H-8sim3.png")},
  {name: ("Stimuli/H5sim0.png"), path:("Stimuli/H5sim0.png")},
  {name: ("Stimuli/H6sim0.png"), path:("Stimuli/H6sim0.png")},
  {name: ("Stimuli/H7sim0.png"), path:("Stimuli/H7sim0.png")},
  {name: ("Stimuli/H8sim0.png"), path:("Stimuli/H8sim0.png")},
  {name: ("Stimuli/dory1.png"), path:("Stimuli/dory1.png")},
  {name: ("Stimuli/dory2.png"), path:("Stimuli/dory2.png")},
  {name: ("Stimuli/nemo1.jpg"), path:("Stimuli/nemo1.jpg")},
  {name: ("Stimuli/nemo2.png"), path:("Stimuli/nemo2.png")},
  {name: ("Designs/design1.csv"), path:("Designs/design1.csv")},
  {name: ("Designs/design2.csv"), path:("Designs/design2.csv")},
  {name: ("Designs/design3.csv"), path:("Designs/design3.csv")},
  {name: ("Designs/design4.csv"), path:("Designs/design4.csv")},
  {name: ("Designs/design5.csv"), path:("Designs/design5.csv")},
  {name: ("Designs/design6.csv"), path:("Designs/design6.csv")},
  {name: ("Designs/design7.csv"), path:("Designs/design7.csv")},
  {name: ("Designs/design8.csv"), path:("Designs/design8.csv")},
  {name: ("Designs/instructions_face_1234.png"), path:("Designs/instructions_face_1234.png")},
  {name: ("Designs/instructions_face_5678.png"), path:("Designs/instructions_face_5678.png")},
  {name: ("Designs/instructions_haus_1234.png"), path:("Designs/instructions_haus_1234.png")},
  {name: ("Designs/instructions_haus_5678.png"), path:("Designs/instructions_haus_5678.png")}]);
  
  expInfo['OS'] = window.navigator.platform;
  expInfo['xResolution'] = screen.width;
  expInfo['yResolution'] = screen.height;
  
  oldt = 0;
  x_size = 8.56;
  y_size = 5.398;
  screen_height = 0;
  if ((win.units === "norm")) {
      x_scale = 0.05;
      y_scale = 0.1;
      dbase = 0.0001;
      unittext = " norm units";
      vsize = 2;
  } else {
      if ((win.units === "pix")) {
          x_scale = 60;
          y_scale = 40;
          dbase = 0.1;
          unittext = " pixels";
          vsize = win.size[1];
      } else {
          x_scale = 0.05;
          y_scale = 0.05;
          dbase = 0.0001;
          unittext = " height units";
          vsize = 1;
      }
  }
  height = 3.459;
  width = 3.459;
  
  text_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_top',
    text: 'Resize this image to match the size of a credit card with arrow keys',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_bottom',
    text: 'Press Space when you’re finished',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  ccimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ccimage', units : undefined, 
    image : 'bankcard.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [(x_size * x_scale), (y_size * y_scale)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "prac_instructions"
  prac_instructionsClock = new util.Clock();
  function shuffle_array(array) {
      for (let i = array.length - 1; i > 0; i--) {
          let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i
  
              // swap elements array[i] and array[j]
              // we use "destructuring assignment" syntax to achieve that
              // you'll find more details about that syntax in later chapters
              // same can be written as:
              // let t = array[i]; array[i] = array[j]; array[j] = t
          [array[i], array[j]] = [array[j], array[i]];
      }
      return array
  }
  
  pracCorr = "";
  corrFix = "";
  pTrial = 0;
  pfix_color_options = ["white", "black"];
  paths = "";
  samepTrials = "";
  diffpTrials = "";
  paths = ["Stimuli/dory1.png", "Stimuli/dory2.png", "Stimuli/nemo1.jpg", "Stimuli/nemo2.png"];
  sameCount = 0;
  diffCount = 0;
  samepTrials = [0, 1, 2, 3];
  shuffle(samepTrials);
  diffpTrials = [[0, 1], [1, 0], [2, 3], [3, 2]];
  shuffle(diffpTrials);
  ptrial_order = [0, 0, 0, 0, 1, 1, 1, 1];
  shuffle(ptrial_order);
  corrpFix = "space";
  numPTrials = 8;
  pfix_switch = [0,0,shuffle_array([1,1,0,0,0,0]),0,0].flat();
  // Initialize components for Routine "prac_target"
  prac_targetClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "prac_probe"
  prac_probeClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  prac_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  prac_fix_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_feedback"
  prac_feedbackClock = new util.Clock();
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "startInstruct"
  startInstructClock = new util.Clock();
  fix_color_options = ["white", "black"];
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      design_file = "Designs/design1.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          design_file = "Designs/design2.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              design_file = "Designs/design3.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
                  design_file = "Designs/design4.csv";
              } else {
                  if ((Number.parseInt(expInfo["design"]) === 5)) {
                      design_file = "Designs/design5.csv";
                  } else {
                      if ((Number.parseInt(expInfo["design"]) === 6)) {
                          design_file = "Designs/design6.csv";
                      } else {
                          if ((Number.parseInt(expInfo["design"]) === 7)) {
                              design_file = "Designs/design7.csv";
                          } else {
                              if ((Number.parseInt(expInfo["design"]) === 8)) {
                                  design_file = "Designs/design8.csv";
                              }
                          }
                      }
                  }
              }
          }
      }
  }
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Now you are ready to play the game!\n\nYou will be doing the same thing you just practiced, but with faces and houses.\n\nPress <SPACE> to see the instructions!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrBlock"
  instrBlockClock = new util.Clock();
  instructions_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "target_img"
  target_imgClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  target_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI_fix"
  ISI_fixClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "probe_img"
  probe_imgClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  probe_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probe_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_resp"
  trial_respClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  good_job = new visual.TextStim({
    win: psychoJS.window,
    name: 'good_job',
    text: 'Great Job!\n\nPress <SPACE> to keep going!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  allDone = new visual.TextStim({
    win: psychoJS.window,
    name: 'allDone',
    text: 'You are all done. Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var screen_scaleComponents;
function screen_scaleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'screen_scale'-------
    t = 0;
    screen_scaleClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    screen_scaleComponents = [];
    screen_scaleComponents.push(text_top);
    screen_scaleComponents.push(text_bottom);
    screen_scaleComponents.push(ccimage);
    
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var keys;
var dscale;
var continueRoutine;
function screen_scaleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'screen_scale'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = screen_scaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys();
    if (keys.length) {
        if (((t - oldt) < 0.5)) {
            dscale = (5 * dbase);
            oldt = t;
        } else {
            dscale = dbase;
            oldt = t;
        }
        if (_pj.in_es6("space", keys)) {
            continueRoutine = false;
        } else {
            if (_pj.in_es6("up", keys)) {
                y_scale = (round(((y_scale + dscale) * 10000)) / 10000);
            } else {
                if (_pj.in_es6("down", keys)) {
                    y_scale = (round(((y_scale - dscale) * 10000)) / 10000);
                } else {
                    if (_pj.in_es6("left", keys)) {
                        x_scale = (round(((x_scale - dscale) * 10000)) / 10000);
                    } else {
                        if (_pj.in_es6("right", keys)) {
                            x_scale = (round(((x_scale + dscale) * 10000)) / 10000);
                        }
                    }
                }
            }
        }
        screen_height = (round(((vsize * 10) / y_scale)) / 10);
        ccimage.size = [(x_size * x_scale), (y_size * y_scale)];
    }
    
    
    // *text_top* updates
    if (t >= 0.0 && text_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_top.tStart = t;  // (not accounting for frame time here)
      text_top.frameNStart = frameN;  // exact frame index
      
      text_top.setAutoDraw(true);
    }

    
    // *text_bottom* updates
    if (t >= 0.0 && text_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_bottom.tStart = t;  // (not accounting for frame time here)
      text_bottom.frameNStart = frameN;  // exact frame index
      
      text_bottom.setAutoDraw(true);
    }

    
    // *ccimage* updates
    if (t >= 0.0 && ccimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ccimage.tStart = t;  // (not accounting for frame time here)
      ccimage.frameNStart = frameN;  // exact frame index
      
      ccimage.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_scaleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'screen_scale'-------
    for (const thisComponent of screen_scaleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    thisExp.addData("X Scale", x_scale);
    thisExp.addData("Y Scale", y_scale);
    
    // the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var rand_Pstart;
var pfix_color;
var prac_instructionsComponents;
function prac_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_instructions'-------
    t = 0;
    prac_instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    rand_Pstart = [0, 1];
    shuffle(rand_Pstart);
    pfix_color = pfix_color_options[rand_Pstart[0]];
    
    // keep track of which components have finished
    prac_instructionsComponents = [];
    
    for (const thisComponent of prac_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function prac_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_instructions'-------
    for (const thisComponent of prac_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "prac_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var pTrials;
var currentLoop;
function pTrialsLoopBegin(pTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  pTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numPTrials, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'pTrials'
  });
  psychoJS.experiment.addLoop(pTrials); // add the loop to the experiment
  currentLoop = pTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPTrial of pTrials) {
    const snapshot = pTrials.getSnapshot();
    pTrialsLoopScheduler.add(importConditions(snapshot));
    pTrialsLoopScheduler.add(prac_targetRoutineBegin(snapshot));
    pTrialsLoopScheduler.add(prac_targetRoutineEachFrame(snapshot));
    pTrialsLoopScheduler.add(prac_targetRoutineEnd(snapshot));
    pTrialsLoopScheduler.add(prac_probeRoutineBegin(snapshot));
    pTrialsLoopScheduler.add(prac_probeRoutineEachFrame(snapshot));
    pTrialsLoopScheduler.add(prac_probeRoutineEnd(snapshot));
    pTrialsLoopScheduler.add(prac_feedbackRoutineBegin(snapshot));
    pTrialsLoopScheduler.add(prac_feedbackRoutineEachFrame(snapshot));
    pTrialsLoopScheduler.add(prac_feedbackRoutineEnd(snapshot));
    pTrialsLoopScheduler.add(endLoopIteration(pTrialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function pTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(pTrials);

  return Scheduler.Event.NEXT;
}


var blocks;
function blocksLoopBegin(blocksLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: design_file,
    seed: undefined, name: 'blocks'
  });
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock of blocks) {
    const snapshot = blocks.getSnapshot();
    blocksLoopScheduler.add(importConditions(snapshot));
    blocksLoopScheduler.add(instrBlockRoutineBegin(snapshot));
    blocksLoopScheduler.add(instrBlockRoutineEachFrame(snapshot));
    blocksLoopScheduler.add(instrBlockRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    blocksLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopEnd);
    blocksLoopScheduler.add(feedbackRoutineBegin(snapshot));
    blocksLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    blocksLoopScheduler.add(feedbackRoutineEnd(snapshot));
    blocksLoopScheduler.add(endLoopIteration(blocksLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numTrials, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(target_imgRoutineBegin(snapshot));
    trialsLoopScheduler.add(target_imgRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(target_imgRoutineEnd(snapshot));
    trialsLoopScheduler.add(ISI_fixRoutineBegin(snapshot));
    trialsLoopScheduler.add(ISI_fixRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ISI_fixRoutineEnd(snapshot));
    trialsLoopScheduler.add(probe_imgRoutineBegin(snapshot));
    trialsLoopScheduler.add(probe_imgRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(probe_imgRoutineEnd(snapshot));
    trialsLoopScheduler.add(trial_respRoutineBegin(snapshot));
    trialsLoopScheduler.add(trial_respRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trial_respRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}


var corrPfix;
var prac_target;
var prac_probe;
var prac_targetComponents;
function prac_targetRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_target'-------
    t = 0;
    prac_targetClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    if ((pfix_switch[pTrial] === 1)) {
        corrPfix = "space";
        if ((pfix_switch === "white")) {
            pfix_color = pfix_color_options[1];
        } else {
            pfix_color = pfix_color_options[0];
        }
    } else {
        pfix_color = pfix_color;
        corrPfix = "";
    }
    console.log(pfix_switch[pTrial]);
    console.log(pfix_color);
    if ((ptrial_order[pTrial] === 0)) {
        prac_target = paths[samepTrials[sameCount]];
        prac_probe = paths[samepTrials[sameCount]];
        if ((Number.parseInt(expInfo["design"]) < 5)) {
            pracCorr = "f";
        } else {
            if ((Number.parseInt(expInfo["design"]) > 4)) {
                pracCorr = "j";
            }
        }
        sameCount = (sameCount + 1);
    } else {
        if ((ptrial_order[pTrial] === 1)) {
            prac_target = paths[diffpTrials[diffCount][0]];
            prac_probe = paths[diffpTrials[diffCount][1]];
            console.log(pracCorr);
            if ((Number.parseInt(expInfo["design"]) < 5)) {
                pracCorr = "j";
            } else {
                if ((Number.parseInt(expInfo["design"]) > 4)) {
                    pracCorr = "f";
                }
            }
            console.log(pracCorr);
            diffCount = (diffCount + 1);
        } else {
            console.log("What is going on");
        }
    }
    
    text_6.setColor(new util.Color(pfix_color));
    image.setImage(prac_target);
    // keep track of which components have finished
    prac_targetComponents = [];
    prac_targetComponents.push(text_6);
    prac_targetComponents.push(image);
    
    for (const thisComponent of prac_targetComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function prac_targetRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_target'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_targetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    frameRemains = 0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_targetComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_targetRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_target'-------
    for (const thisComponent of prac_targetComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _prac_resp_allKeys;
var _prac_fix_resp_allKeys;
var prac_probeComponents;
function prac_probeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_probe'-------
    t = 0;
    prac_probeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    text_7.setColor(new util.Color(pfix_color));
    image_2.setImage(prac_probe);
    prac_resp.keys = undefined;
    prac_resp.rt = undefined;
    _prac_resp_allKeys = [];
    prac_fix_resp.keys = undefined;
    prac_fix_resp.rt = undefined;
    _prac_fix_resp_allKeys = [];
    // keep track of which components have finished
    prac_probeComponents = [];
    prac_probeComponents.push(text_7);
    prac_probeComponents.push(image_2);
    prac_probeComponents.push(prac_resp);
    prac_probeComponents.push(prac_fix_resp);
    
    for (const thisComponent of prac_probeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function prac_probeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_probe'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_probeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    
    // *prac_resp* updates
    if (t >= 0.2 && prac_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_resp.tStart = t;  // (not accounting for frame time here)
      prac_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_resp.clearEvents(); });
    }

    if (prac_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _prac_resp_allKeys = _prac_resp_allKeys.concat(theseKeys);
      if (_prac_resp_allKeys.length > 0) {
        prac_resp.keys = _prac_resp_allKeys[_prac_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_resp.rt = _prac_resp_allKeys[_prac_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_resp.keys == pracCorr) {
            prac_resp.corr = 1;
        } else {
            prac_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *prac_fix_resp* updates
    if (t >= 0.2 && prac_fix_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_fix_resp.tStart = t;  // (not accounting for frame time here)
      prac_fix_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_fix_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_fix_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_fix_resp.clearEvents(); });
    }

    if (prac_fix_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_fix_resp.getKeys({keyList: ['space'], waitRelease: false});
      _prac_fix_resp_allKeys = _prac_fix_resp_allKeys.concat(theseKeys);
      if (_prac_fix_resp_allKeys.length > 0) {
        prac_fix_resp.keys = _prac_fix_resp_allKeys[_prac_fix_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_fix_resp.rt = _prac_fix_resp_allKeys[_prac_fix_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_fix_resp.keys == corrPfix) {
            prac_fix_resp.corr = 1;
        } else {
            prac_fix_resp.corr = 0;
        }
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_probeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_probeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_probe'-------
    for (const thisComponent of prac_probeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (prac_resp.keys === undefined) {
      if (['None','none',undefined].includes(pracCorr)) {
         prac_resp.corr = 1;  // correct non-response
      } else {
         prac_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('prac_resp.keys', prac_resp.keys);
    psychoJS.experiment.addData('prac_resp.corr', prac_resp.corr);
    if (typeof prac_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_resp.rt', prac_resp.rt);
        routineTimer.reset();
        }
    
    prac_resp.stop();
    // was no response the correct answer?!
    if (prac_fix_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrPfix)) {
         prac_fix_resp.corr = 1;  // correct non-response
      } else {
         prac_fix_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('prac_fix_resp.keys', prac_fix_resp.keys);
    psychoJS.experiment.addData('prac_fix_resp.corr', prac_fix_resp.corr);
    if (typeof prac_fix_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_fix_resp.rt', prac_fix_resp.rt);
        }
    
    prac_fix_resp.stop();
    // the Routine "prac_probe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedIM;
var prac_feedbackComponents;
function prac_feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_feedback'-------
    t = 0;
    prac_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedIM = "";
    if ((prac_resp.keys === pracCorr)) {
        feedIM = "Stimuli/greenCheck.png";
    } else {
        if ((prac_resp.keys !== pracCorr)) {
            feedIM = "Stimuli/redWrong.png";
        }
    }
    
    image_3.setImage(feedIM);
    // keep track of which components have finished
    prac_feedbackComponents = [];
    prac_feedbackComponents.push(image_3);
    
    for (const thisComponent of prac_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function prac_feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prac_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_feedback'-------
    for (const thisComponent of prac_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    pTrial = (pTrial + 1);
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var startInstructComponents;
function startInstructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'startInstruct'-------
    t = 0;
    startInstructClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    startInstructComponents = [];
    startInstructComponents.push(text_3);
    startInstructComponents.push(key_resp_7);
    
    for (const thisComponent of startInstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function startInstructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'startInstruct'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = startInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startInstructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startInstructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'startInstruct'-------
    for (const thisComponent of startInstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "startInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instruction_img;
var trialSame;
var trialDiff;
var diffTrial;
var sameTrialid;
var diffTrialid;
var sameTrial_left_id;
var diffTrial_left_id;
var sameTrial_right_id;
var diffTrial_right_id;
var trialID;
var rand_start;
var fix_color;
var numTrials;
var trial_order;
var trialSame_left;
var trialDiff_left;
var diffTrial_left;
var trialSame_right;
var trialDiff_right;
var diffTrial_right;
var fix_switch;
var side_same;
var side_diff;
var _key_resp_2_allKeys;
var instrBlockComponents;
function instrBlockRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instrBlock'-------
    t = 0;
    instrBlockClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // add-on: list(s: string): string[]
    function list(s) {
        // if s is a string, we return a list of its characters
        if (typeof s === 'string')
            return s.split('');
        else
            // otherwise we return s:
            return s;
    }
    
    function shuffle_array(array) {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i
    
                // swap elements array[i] and array[j]
                // we use "destructuring assignment" syntax to achieve that
                // you'll find more details about that syntax in later chapters
                // same can be written as:
                // let t = array[i]; array[i] = array[j]; array[j] = t
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array
    }
    
    function divide_subPoint1(array, divisor) {
        let array_divided = array.map(function(element) {
            return element/divisor - 0.1;
        });
        return array_divided
    }
    
    function round_array(array) {
        array = array.map(function(each_element){
            return Math.round(each_element);
        }); 
        return array
    }
    
    if ((Block_type === "conf_face")) {
        paths = ["Stimuli/edmd.png", "Stimuli/eimd.png", "Stimuli/eomu.png", "Stimuli/eumu.png"];
        if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
            instruction_img = "Designs/instructions_face_1234.png";
        } else {
            instruction_img = "Designs/instructions_face_5678.png";
        }
    } else {
        if ((Block_type === "conf_haus")) {
            paths = ["Stimuli/H-8sim0.png", "Stimuli/H-8sim1.png", "Stimuli/H-8sim2.png", "Stimuli/H-8sim3.png"];
            if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                instruction_img = "Designs/instructions_haus_1234.png";
            } else {
                instruction_img = "Designs/instructions_haus_5678.png";
            }
        } else {
            if ((Block_type === "feat_face")) {
                paths = ["Stimuli/f15.png", "Stimuli/f24.png", "Stimuli/f131.png", "Stimuli/f142.png"];
                if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                    instruction_img = "Designs/instructions_face_1234.png";
                } else {
                    instruction_img = "Designs/instructions_face_5678.png";
                }
            } else {
                if ((Block_type === "feat_haus")) {
                    paths = ["Stimuli/H5sim0.png", "Stimuli/H6sim0.png", "Stimuli/H7sim0.png", "Stimuli/H8sim0.png"];
                    if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                        instruction_img = "Designs/instructions_haus_1234.png";
                    } else {
                        instruction_img = "Designs/instructions_haus_5678.png";
                    }
                }
            }
        }
    }
    
    trialSame = 0;
    trialDiff = 0;
    diffTrial = 0;
    sameTrialid = -1;
    diffTrialid = -1;
    sameTrial_left_id = -1;
    diffTrial_left_id = -1;
    sameTrial_right_id = -1;
    diffTrial_right_id = -1;
    trialID = -1;
    rand_start = shuffle_array([0,1]);
    fix_color = fix_color_options[rand_start[0]];
    
    if ((Number.parseInt(expInfo["position"]) === 2)) {
        console.log(numTrials)
        numTrials = 48;
        console.log(numTrials)
        trial_order = [shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]),shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6])].flat();
        trial_order = round_array(divide_subPoint1(trial_order,6))
        trialSame_left = [shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3])].flat();
        trialDiff_left = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 0], [2, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]];
        diffTrial_left = shuffle_array(list([...Array(12).keys()]));
        trialSame_right = [shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3])].flat();
        trialDiff_right = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 0], [2, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]];
        diffTrial_right = shuffle_array(list([...Array(12).keys()]));
        fix_switch = [0,0,shuffle_array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]),0,0].flat();
        side_same = shuffle_array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]);
        side_diff = shuffle_array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]);
    } else {
        if ((Number.parseInt(expInfo["position"]) === 1)) {
            numTrials = 24;
            trial_order = [shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6])].flat();
            trial_order = round_array(divide_subPoint1(trial_order,6))
            trialSame = [shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3])].flat();
            trialDiff = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 0], [2, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]];
            diffTrial = shuffle_array(list([...Array(12).keys()]));
            fix_switch = [0,0,shuffle_array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),0,0].flat();
            //        side = shuffle_array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]);
        } else {
            if ((Number.parseInt(expInfo["position"]) === 3)) {
                numTrials = 24;
                trial_order = [shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6]), shuffle_array([1, 2, 3, 4, 5, 6])].flat();
                trial_order = round_array(divide_subPoint1(trial_order,6))
                trialSame = [shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3]), shuffle_array([0, 1, 2, 3])].flat();
                trialDiff = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 0], [2, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]];
                diffTrial = shuffle_array(list([...Array(12).keys()]));
                fix_switch = [0,0,shuffle_array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),0,0].flat();
                //            side = shuffle_array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
            }
        }
    }
    
    
    instructions_image.setImage(instruction_img);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instrBlockComponents = [];
    instrBlockComponents.push(instructions_image);
    instrBlockComponents.push(key_resp_2);
    
    for (const thisComponent of instrBlockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instrBlockRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instrBlock'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_image* updates
    if (t >= 0.0 && instructions_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_image.tStart = t;  // (not accounting for frame time here)
      instructions_image.frameNStart = frameN;  // exact frame index
      
      instructions_image.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 1 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrBlockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrBlockRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instrBlock'-------
    for (const thisComponent of instrBlockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instrBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var img_pair;
var target;
var probe;
var corr;
var xPosition;
var _key_resp_3_allKeys;
var target_imgComponents;
function target_imgRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'target_img'-------
    t = 0;
    target_imgClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    img_pair = 0;
    target = 0;
    probe = 0;
    corr = 0;
    trialID = (trialID + 1);
    if ((fix_switch[trialID] === 1)) {
        if ((fix_color === "pink")) {
            fix_color = fix_color_options[1];
        } else {
            fix_color = fix_color_options[0];
        }
    }
    if ((Number.parseInt(expInfo["position"]) === 0)) {
        xPosition = 0;
    } else {
        if ((Number.parseInt(expInfo["position"]) === 2)) {
            if ((trial_order[trialID] === 1)) {
                sameTrialid += 1;
                if ((side_same[sameTrialid] === 1)) {
                    xPosition = (- (width * x_scale));
                    sameTrial_left_id += 1;
                    console.log(("left same ID: " + sameTrial_left_id.toString()));
                    target = paths[trialSame_left[sameTrial_left_id]];
                    probe = paths[trialSame_left[sameTrial_left_id]];
                    if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                        corr = "f";
                    } else {
                        corr = "j";
                    }
                } else {
                    if ((side_same[sameTrialid] === 0)) {
                        xPosition = (width * x_scale);
                        sameTrial_right_id += 1;
                        console.log(("right same ID: " + sameTrial_right_id.toString()));
                        target = paths[trialSame_right[sameTrial_right_id]];
                        probe = paths[trialSame_right[sameTrial_right_id]];
                        if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                            corr = "f";
                        } else {
                            corr = "j";
                        }
                    }
                }
            } else {
                if ((trial_order[trialID] === 0)) {
                    diffTrialid += 1;
                    if ((side_diff[diffTrialid] === 1)) {
                        xPosition = (- (width * x_scale));
                        diffTrial_left_id += 1;
                        console.log(("left diff ID: " + diffTrial_left_id.toString()));
                        img_pair = trialDiff_left[diffTrial_left[diffTrial_left_id]];
                        target = paths[img_pair[0]];
                        probe = paths[img_pair[1]];
                        if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                            corr = "j";
                        } else {
                            corr = "f";
                        }
                    } else {
                        if ((side_diff[diffTrialid] === 0)) {
                            xPosition = (width * x_scale);
                            diffTrial_right_id += 1;
                            console.log(("right diff ID: " + diffTrial_right_id.toString()));
                            img_pair = trialDiff_right[diffTrial_right[diffTrial_right_id]];
                            target = paths[img_pair[0]];
                            probe = paths[img_pair[1]];
                            if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                                corr = "j";
                            } else {
                                corr = "f";
                            }
                        }
                    }
                }
            }
        } else {
            if ((Number.parseInt(expInfo["position"]) === 1)) {
                xPosition = (- (width * x_scale));
                if ((trial_order[trialID] === 1)) {
                    sameTrialid += 1;
                    target = paths[trialSame[sameTrialid]];
                    probe = paths[trialSame[sameTrialid]];
                    if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                        corr = "f";
                    } else {
                        corr = "j";
                    }
                } else {
                    if ((trial_order[trialID] === 0)) {
                        diffTrialid += 1;
                        img_pair = trialDiff[diffTrial[diffTrialid]];
                        target = paths[img_pair[0]];
                        probe = paths[img_pair[1]];
                        if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                            corr = "j";
                        } else {
                            corr = "f";
                        }
                    }
                }
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width * x_scale);
                    if ((trial_order[trialID] === 1)) {
                        sameTrialid += 1;
                        target = paths[trialSame[sameTrialid]];
                        probe = paths[trialSame[sameTrialid]];
                        if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                            corr = "f";
                        } else {
                            corr = "j";
                        }
                    } else {
                        if ((trial_order[trialID] === 0)) {
                            diffTrialid += 1;
                            img_pair = trialDiff[diffTrial[diffTrialid]];
                            target = paths[img_pair[0]];
                            probe = paths[img_pair[1]];
                            if (((((Number.parseInt(expInfo["design"]) === (1 | Number.parseInt(expInfo["design"]))) && ((1 | Number.parseInt(expInfo["design"])) === (2 | Number.parseInt(expInfo["design"])))) && ((2 | Number.parseInt(expInfo["design"])) === (3 | Number.parseInt(expInfo["design"])))) && ((3 | Number.parseInt(expInfo["design"])) === 4))) {
                                corr = "j";
                            } else {
                                corr = "f";
                            }
                        }
                    }
                }
            }
        }
    }
    thisExp.addData("fix_switches", fix_switch[trialID]);
    thisExp.addData("side", xPosition);
    thisExp.addData("trial_type1S0D", trial_order[trialID]);
    thisExp.addData("target", target);
    thisExp.addData("probe", probe);
    
    text_4.setColor(new util.Color(fix_color));
    target_image.setPos([xPosition, 0]);
    target_image.setSize([(width * x_scale), (height * y_scale)]);
    target_image.setImage(target);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    target_imgComponents = [];
    target_imgComponents.push(text_4);
    target_imgComponents.push(target_image);
    target_imgComponents.push(key_resp_3);
    
    for (const thisComponent of target_imgComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function target_imgRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'target_img'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = target_imgClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    
    // *target_image* updates
    if (t >= 0.0 && target_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_image.tStart = t;  // (not accounting for frame time here)
      target_image.frameNStart = frameN;  // exact frame index
      
      target_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_image.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of target_imgComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function target_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'target_img'-------
    for (const thisComponent of target_imgComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        }
    
    key_resp_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var ISI_fixComponents;
function ISI_fixRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ISI_fix'-------
    t = 0;
    ISI_fixClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    text.setColor(new util.Color(fix_color));
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    ISI_fixComponents = [];
    ISI_fixComponents.push(text);
    ISI_fixComponents.push(key_resp_4);
    
    for (const thisComponent of ISI_fixComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function ISI_fixRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ISI_fix'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ISI_fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ISI_fixComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISI_fixRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ISI_fix'-------
    for (const thisComponent of ISI_fixComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        }
    
    key_resp_4.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var probe_imgComponents;
function probe_imgRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'probe_img'-------
    t = 0;
    probe_imgClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    text_5.setColor(new util.Color(fix_color));
    probe_image.setPos([xPosition, 0]);
    probe_image.setSize([(width * x_scale), (height * y_scale)]);
    probe_image.setImage(probe);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    probe_imgComponents = [];
    probe_imgComponents.push(text_5);
    probe_imgComponents.push(probe_image);
    probe_imgComponents.push(key_resp_5);
    
    for (const thisComponent of probe_imgComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function probe_imgRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'probe_img'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = probe_imgClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    
    // *probe_image* updates
    if (t >= 0 && probe_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_image.tStart = t;  // (not accounting for frame time here)
      probe_image.frameNStart = frameN;  // exact frame index
      
      probe_image.setAutoDraw(true);
    }

    frameRemains = 0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (probe_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      probe_image.setAutoDraw(false);
    }
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_5.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of probe_imgComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function probe_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'probe_img'-------
    for (const thisComponent of probe_imgComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        }
    
    key_resp_5.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var _key_resp_6_allKeys;
var trial_respComponents;
function trial_respRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_resp'-------
    t = 0;
    trial_respClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    text_2.setColor(new util.Color(fix_color));
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    trial_respComponents = [];
    trial_respComponents.push(text_2);
    trial_respComponents.push(key_resp);
    trial_respComponents.push(key_resp_6);
    
    for (const thisComponent of trial_respComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial_respRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial_resp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial_respClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == corr) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_respComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_respRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_resp'-------
    for (const thisComponent of trial_respComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        }
    
    key_resp_6.stop();
    // the Routine "trial_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(good_job);
    feedbackComponents.push(key_resp_8);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *good_job* updates
    if (t >= 0.0 && good_job.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      good_job.tStart = t;  // (not accounting for frame time here)
      good_job.frameNStart = frameN;  // exact frame index
      
      good_job.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(allDone);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EndScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *allDone* updates
    if (t >= 0.0 && allDone.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      allDone.tStart = t;  // (not accounting for frame time here)
      allDone.frameNStart = frameN;  // exact frame index
      
      allDone.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (allDone.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      allDone.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
