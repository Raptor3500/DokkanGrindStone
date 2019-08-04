import peewee #line:1
from peewee import *#line:2
class DatabaseProxyToggle :#line:5
    _db_glb :SqliteDatabase =None #line:6
    _db_jp :SqliteDatabase =None #line:7
    current_db :SqliteDatabase =None #line:8
    proxy =DatabaseProxy ()#line:9
    def __init__ (OOOOOO0O0OO0OO00O ,OOO0OOOO00O0OO00O :str ,OO0O00OO00000O0OO :str ):#line:11
        OOOOOO0O0OO0OO00O ._db_glb =SqliteDatabase (OOO0OOOO00O0OO00O )#line:12
        OOOOOO0O0OO0OO00O ._db_jp =SqliteDatabase (OO0O00OO00000O0OO )#line:13
        OOOOOO0O0OO0OO00O ._db_glb .connect ()#line:14
        OOOOOO0O0OO0OO00O ._db_jp .connect ()#line:15
        OOOOOO0O0OO0OO00O .set_glb ()#line:16
    def set_glb (OOO0O0OOO0OO00O0O ):#line:18
        OOO0O0OOO0OO00O0O .current_db =OOO0O0OOO0OO00O0O ._db_glb #line:19
        OOO0O0OOO0OO00O0O .proxy .initialize (OOO0O0OOO0OO00O0O .current_db )#line:20
    def set_jp (OO0O0OOOO00OO000O ):#line:22
        OO0O0OOOO00OO000O .current_db =OO0O0OOOO00OO000O ._db_jp #line:23
        OO0O0OOOO00OO000O .proxy .initialize (OO0O0OOOO00OO000O .current_db )#line:24
    def is_glb (OO0OOOOOO0OO00OO0 )->bool :#line:26
        return OO0OOOOOO0OO00OO0 .current_db ==OO0OOOOOO0OO00OO0 ._db_glb #line:27
    def is_jp (OO0O00O0O0OOO000O )->bool :#line:29
        return OO0O00O0O0OOO000O .current_db ==OO0O00O0O0OOO000O ._db_jp #line:30
    def toggle (O00O0OO0OO00OOOO0 ):#line:32
        if O00O0OO0OO00OOOO0 .is_glb ():#line:33
            O00O0OO0OO00OOOO0 .set_jp ()#line:34
        else :#line:35
            O00O0OO0OO00OOOO0 .set_glb ()#line:36
db =DatabaseProxyToggle ('glb.db','jp.db')#line:39
class FailoverModelSelect (peewee .ModelSelect ):#line:42
    def get (OOO0O00O0OO0O00O0 ,database =None ):#line:43
        global db #line:44
        try :#line:45
            O0OO00O0OOO00O00O =super ().get (db .current_db )#line:46
        except peewee .DoesNotExist :#line:47
            db .toggle ()#line:48
            try :#line:49
                O0OO00O0OOO00O00O =super ().get (db .current_db )#line:50
            finally :#line:51
                db .toggle ()#line:52
        return O0OO00O0OOO00O00O #line:53
class BaseModel (Model ):#line:56
    class Meta :#line:57
        database =db .proxy #line:58
    @classmethod #line:60
    def select (O000000OOOOO0OOO0 ,*O0000O000OOOOO00O ):#line:61
        O00O000OO00O0O0O0 =not O0000O000OOOOO00O #line:62
        if not O0000O000OOOOO00O :#line:63
            O0000O000OOOOO00O =O000000OOOOO0OOO0 ._meta .sorted_fields #line:64
        return FailoverModelSelect (O000000OOOOO0OOO0 ,O0000O000OOOOO00O ,is_default =O00O000OO00O0O0O0 )#line:65
class ActCureSchedules (BaseModel ):#line:68
    created_at =DateTimeField (null =True )#line:69
    end_at =DateTimeField ()#line:70
    seconds_per_cure_one_act =IntegerField ()#line:71
    start_at =DateTimeField ()#line:72
    updated_at =DateTimeField (null =True )#line:73
    class Meta :#line:75
        table_name ='act_cure_schedules'#line:76
class ActItems (BaseModel ):#line:79
    created_at =DateTimeField ()#line:80
    description =CharField ()#line:81
    id =BigAutoField ()#line:82
    name =CharField ()#line:83
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:84
    recover_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:85
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:86
    updated_at =DateTimeField ()#line:87
    class Meta :#line:89
        table_name ='act_items'#line:90
class ActiveSkillSets (BaseModel ):#line:93
    bgm_id =IntegerField (null =True )#line:94
    condition_description =TextField ()#line:95
    created_at =DateTimeField ()#line:96
    effect_description =TextField ()#line:97
    exec_limit =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:98
    id =BigAutoField ()#line:99
    name =CharField ()#line:100
    skill_causality_set_id =IntegerField (null =True )#line:101
    special_view_id =IntegerField (null =True )#line:102
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:103
    ultimate_special_id =IntegerField (null =True )#line:104
    updated_at =DateTimeField ()#line:105
    class Meta :#line:107
        table_name ='active_skill_sets'#line:108
class ActiveSkills (BaseModel ):#line:111
    active_skill_set_id =IntegerField (index =True )#line:112
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:113
    created_at =DateTimeField ()#line:114
    eff_val1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:115
    eff_val2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:116
    eff_val3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:117
    effect_se_id =IntegerField (null =True )#line:118
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:119
    id =BigAutoField ()#line:120
    sub_target_type_set_id =IntegerField (null =True )#line:121
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:122
    thumb_effect_id =IntegerField (null =True )#line:123
    updated_at =DateTimeField ()#line:124
    class Meta :#line:126
        table_name ='active_skills'#line:127
class AreaConditions (BaseModel ):#line:130
    area_id =IntegerField (index =True )#line:131
    comment =CharField ()#line:132
    conditions =TextField (null =True )#line:133
    created_at =DateTimeField (null =True )#line:134
    type =CharField ()#line:135
    updated_at =DateTimeField (null =True )#line:136
    class Meta :#line:138
        table_name ='area_conditions'#line:139
class AreaIcons (BaseModel ):#line:142
    created_at =DateTimeField (null =True )#line:143
    icon_x =IntegerField (null =True )#line:144
    icon_y =IntegerField (null =True )#line:145
    image =CharField (null =True )#line:146
    updated_at =DateTimeField (null =True )#line:147
    world_id =IntegerField (index =True )#line:148
    class Meta :#line:150
        table_name ='area_icons'#line:151
class AreaTabs (BaseModel ):#line:154
    area_category_ids =CharField (null =True )#line:155
    created_at =DateTimeField (null =True )#line:156
    name =CharField (null =True )#line:157
    updated_at =DateTimeField (null =True )#line:158
    class Meta :#line:160
        table_name ='area_tabs'#line:161
class Areas (BaseModel ):#line:164
    all_clear_bonus_stones =IntegerField (null =True )#line:165
    announcement_id =IntegerField (index =True ,null =True )#line:166
    area_icon_id =IntegerField (null =True )#line:167
    banner_image =CharField (null =True )#line:168
    bgm_id =IntegerField (null =True )#line:169
    category =IntegerField (null =True )#line:170
    created_at =DateTimeField (null =True )#line:171
    event_image =CharField (null =True )#line:172
    event_priority =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:173
    first_released_at =DateTimeField (null =True )#line:174
    height =IntegerField (null =True )#line:175
    is_listbutton_visible =IntegerField ()#line:176
    is_quest_num_visible =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:177
    layer0 =CharField (null =True )#line:178
    layer1 =CharField (null =True )#line:179
    layer2 =CharField (null =True )#line:180
    layer3 =CharField (null =True )#line:181
    listbutton_image =CharField (null =True )#line:182
    locked_by =CharField (null =True )#line:183
    minibanner_image =CharField (null =True )#line:184
    name =CharField ()#line:185
    prev_area_id =IntegerField (index =True ,null =True )#line:186
    split =IntegerField (null =True )#line:187
    type =CharField (null =True )#line:188
    updated_at =DateTimeField (null =True )#line:189
    width =IntegerField (null =True )#line:190
    world_id =IntegerField (index =True )#line:191
    class Meta :#line:193
        table_name ='areas'#line:194
class AwakeningItems (BaseModel ):#line:197
    created_at =DateTimeField (null =True )#line:198
    description =CharField ()#line:199
    event_jumpable =IntegerField (constraints =[SQL ("DEFAULT '1'")],null =True )#line:200
    name =CharField ()#line:201
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:202
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:203
    updated_at =DateTimeField (null =True )#line:204
    zeni =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:205
    class Meta :#line:207
        table_name ='awakening_items'#line:208
class BattleParams (BaseModel ):#line:211
    created_at =DateTimeField (null =True )#line:212
    idx =IntegerField ()#line:213
    param_no =IntegerField (index =True )#line:214
    updated_at =DateTimeField (null =True )#line:215
    value =IntegerField ()#line:216
    class Meta :#line:218
        table_name ='battle_params'#line:219
class BeginnersGuides (BaseModel ):#line:222
    created_at =DateTimeField (null =True )#line:223
    name =CharField ()#line:224
    start_at =DateTimeField ()#line:225
    start_image =CharField ()#line:226
    updated_at =DateTimeField (null =True )#line:227
    class Meta :#line:229
        table_name ='beginners_guides'#line:230
class BgmSchedules (BaseModel ):#line:233
    bgm_id =IntegerField ()#line:234
    created_at =DateTimeField ()#line:235
    end_at =DateTimeField ()#line:236
    id =BigAutoField ()#line:237
    scene_name =CharField ()#line:238
    start_at =DateTimeField ()#line:239
    updated_at =DateTimeField ()#line:240
    class Meta :#line:242
        table_name ='bgm_schedules'#line:243
class BoostSchedules (BaseModel ):#line:246
    created_at =DateTimeField ()#line:247
    end_at =DateTimeField ()#line:248
    id =BigAutoField ()#line:249
    max_point =IntegerField ()#line:250
    seconds_per_cure_one_point =IntegerField ()#line:251
    start_at =DateTimeField ()#line:252
    updated_at =DateTimeField ()#line:253
    class Meta :#line:255
        table_name ='boost_schedules'#line:256
class BudokaiBoxRankingRewardRanges (BaseModel ):#line:259
    budokai_box_ranking_id =IntegerField (index =True )#line:260
    created_at =DateTimeField (null =True )#line:261
    end_value =IntegerField ()#line:262
    start_value =IntegerField ()#line:263
    updated_at =DateTimeField (null =True )#line:264
    class Meta :#line:266
        table_name ='budokai_box_ranking_reward_ranges'#line:267
class BudokaiBoxRankingRewards (BaseModel ):#line:270
    budokai_box_ranking_reward_range_id =IntegerField (index =True )#line:271
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:272
    created_at =DateTimeField (null =True )#line:273
    description =CharField ()#line:274
    gift_description =CharField ()#line:275
    item_id =IntegerField ()#line:276
    item_type =CharField ()#line:277
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:278
    updated_at =DateTimeField (null =True )#line:279
    class Meta :#line:281
        table_name ='budokai_box_ranking_rewards'#line:282
class BudokaiBoxRankings (BaseModel ):#line:285
    box_max_count =IntegerField (null =True )#line:286
    budokai_id =IntegerField (index =True )#line:287
    collecting_end_at =DateTimeField ()#line:288
    created_at =DateTimeField (null =True )#line:289
    end_at =DateTimeField ()#line:290
    player_max_count =IntegerField ()#line:291
    prev_budokai_box_ranking_id =IntegerField (null =True )#line:292
    prev_budokai_id =IntegerField (null =True )#line:293
    start_at =DateTimeField ()#line:294
    updated_at =DateTimeField (null =True )#line:295
    class Meta :#line:297
        table_name ='budokai_box_rankings'#line:298
class BudokaiHelpBodies (BaseModel ):#line:301
    budokai_help_id =IntegerField (index =True ,null =True )#line:302
    created_at =DateTimeField (null =True )#line:303
    description =TextField (null =True )#line:304
    image =CharField (null =True )#line:305
    updated_at =DateTimeField (null =True )#line:306
    class Meta :#line:308
        table_name ='budokai_help_bodies'#line:309
class BudokaiHelpCategories (BaseModel ):#line:312
    created_at =DateTimeField (null =True )#line:313
    num =IntegerField (null =True )#line:314
    title =CharField ()#line:315
    updated_at =DateTimeField (null =True )#line:316
    class Meta :#line:318
        table_name ='budokai_help_categories'#line:319
class BudokaiHelps (BaseModel ):#line:322
    budokai_help_category_id =IntegerField ()#line:323
    created_at =DateTimeField (null =True )#line:324
    description =TextField (null =True )#line:325
    num =IntegerField (null =True )#line:326
    title =CharField ()#line:327
    updated_at =DateTimeField (null =True )#line:328
    class Meta :#line:330
        table_name ='budokai_helps'#line:331
class BudokaiLeagues (BaseModel ):#line:334
    budokai_id =IntegerField ()#line:335
    created_at =DateTimeField (null =True )#line:336
    league =IntegerField ()#line:337
    name =CharField ()#line:338
    updated_at =DateTimeField (null =True )#line:339
    class Meta :#line:341
        table_name ='budokai_leagues'#line:342
        indexes =((('budokai_id','league'),False ),)#line:343
class BudokaiMissionRewards (BaseModel ):#line:346
    budokai_mission_id =IntegerField (index =True )#line:347
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:348
    created_at =DateTimeField (null =True )#line:349
    description =CharField ()#line:350
    gift_description =CharField ()#line:351
    item_id =IntegerField ()#line:352
    item_type =CharField ()#line:353
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:354
    updated_at =DateTimeField (null =True )#line:355
    class Meta :#line:357
        table_name ='budokai_mission_rewards'#line:358
class BudokaiMissions (BaseModel ):#line:361
    budokai_id =IntegerField ()#line:362
    created_at =DateTimeField (null =True )#line:363
    mission_type =IntegerField ()#line:364
    name =CharField ()#line:365
    prev_budokai_mission_id =IntegerField (null =True )#line:366
    priority =IntegerField ()#line:367
    target_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:368
    updated_at =DateTimeField (null =True )#line:369
    class Meta :#line:371
        table_name ='budokai_missions'#line:372
        indexes =((('budokai_id','mission_type'),False ),)#line:373
class BudokaiMotivationUnlockConditions (BaseModel ):#line:376
    budokai_motivation_id =IntegerField (index =True )#line:377
    conditions =TextField (null =True )#line:378
    created_at =DateTimeField (null =True )#line:379
    description =CharField (null =True )#line:380
    type =CharField (null =True )#line:381
    updated_at =DateTimeField (null =True )#line:382
    class Meta :#line:384
        table_name ='budokai_motivation_unlock_conditions'#line:385
class BudokaiMotivations (BaseModel ):#line:388
    additional_atk_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:389
    additional_def_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:390
    additional_hp_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:391
    additional_point_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:392
    announcer_description =CharField (null =True )#line:393
    budokai_id =IntegerField (index =True )#line:394
    created_at =DateTimeField (null =True )#line:395
    max_atk_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:396
    max_def_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:397
    max_hp_percent =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:398
    player_description =CharField ()#line:399
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:400
    updated_at =DateTimeField (null =True )#line:401
    class Meta :#line:403
        table_name ='budokai_motivations'#line:404
class BudokaiOpponentAttackWeightLines (BaseModel ):#line:407
    ball_count =IntegerField ()#line:408
    budokai_opponent_attack_weight_id =IntegerField ()#line:409
    rate =IntegerField ()#line:410
    class Meta :#line:412
        table_name ='budokai_opponent_attack_weight_lines'#line:413
class BudokaiOpponentAttackWeights (BaseModel ):#line:416
    budokai_id =IntegerField ()#line:417
    created_at =DateTimeField (null =True )#line:418
    round =IntegerField ()#line:419
    updated_at =DateTimeField (null =True )#line:420
    class Meta :#line:422
        table_name ='budokai_opponent_attack_weights'#line:423
class BudokaiProgressSelifs (BaseModel ):#line:426
    budokai_id =IntegerField ()#line:427
    description =TextField (null =True )#line:428
    round =IntegerField ()#line:429
    url =CharField (null =True )#line:430
    class Meta :#line:432
        table_name ='budokai_progress_selifs'#line:433
class BudokaiRankingGiftSets (BaseModel ):#line:436
    budokai_id =IntegerField ()#line:437
    created_at =DateTimeField (null =True )#line:438
    order =IntegerField ()#line:439
    ranking =CharField ()#line:440
    updated_at =DateTimeField (null =True )#line:441
    class Meta :#line:443
        table_name ='budokai_ranking_gift_sets'#line:444
        indexes =((('budokai_id','order'),False ),)#line:445
class BudokaiRankingGifts (BaseModel ):#line:448
    budokai_ranking_gift_set_id =IntegerField (index =True )#line:449
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:450
    created_at =DateTimeField (null =True )#line:451
    description =CharField (null =True )#line:452
    item_id =IntegerField ()#line:453
    item_type =CharField ()#line:454
    quantity =IntegerField ()#line:455
    updated_at =DateTimeField (null =True )#line:456
    class Meta :#line:458
        table_name ='budokai_ranking_gifts'#line:459
class BudokaiRanks (BaseModel ):#line:462
    bonus =FloatField (constraints =[SQL ("DEFAULT '1'")])#line:463
    budokai_id =IntegerField ()#line:464
    budokai_league_id =IntegerField ()#line:465
    created_at =DateTimeField (null =True )#line:466
    name =CharField ()#line:467
    point =IntegerField ()#line:468
    rank =IntegerField ()#line:469
    updated_at =DateTimeField (null =True )#line:470
    class Meta :#line:472
        table_name ='budokai_ranks'#line:473
        indexes =((('budokai_id','rank'),False ),)#line:474
class Budokais (BaseModel ):#line:477
    banner_image =CharField ()#line:478
    collecting_end_at =DateTimeField ()#line:479
    created_at =DateTimeField (null =True )#line:480
    description =TextField ()#line:481
    description_script_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:482
    end_at =DateTimeField ()#line:483
    entry_script_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:484
    listbutton_image =CharField (null =True )#line:485
    mission_reward_image_url =CharField ()#line:486
    name =CharField ()#line:487
    result_end_at =DateTimeField ()#line:488
    start_at =DateTimeField ()#line:489
    updated_at =DateTimeField (null =True )#line:490
    class Meta :#line:492
        table_name ='budokais'#line:493
class CardActiveSkills (BaseModel ):#line:496
    active_skill_set_id =IntegerField ()#line:497
    card_id =IntegerField (index =True )#line:498
    created_at =DateTimeField ()#line:499
    id =BigAutoField ()#line:500
    updated_at =DateTimeField ()#line:501
    class Meta :#line:503
        table_name ='card_active_skills'#line:504
class CardAwakeningRoutes (BaseModel ):#line:507
    awaked_card_id =IntegerField (index =True ,null =True )#line:508
    card_awakening_set_id =IntegerField (index =True )#line:509
    card_id =IntegerField (index =True )#line:510
    created_at =DateTimeField (null =True )#line:511
    description =TextField (null =True )#line:512
    num =IntegerField (null =True )#line:513
    open_at =DateTimeField (constraints =[SQL ("DEFAULT '2010-04-01 00:00:00'")],null =True )#line:514
    optimal_awakening_step =IntegerField (null =True )#line:515
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")],null =True )#line:516
    type =CharField ()#line:517
    updated_at =DateTimeField (null =True )#line:518
    class Meta :#line:520
        table_name ='card_awakening_routes'#line:521
class CardAwakeningSets (BaseModel ):#line:524
    created_at =DateTimeField (null =True )#line:525
    description =CharField (null =True )#line:526
    name =CharField (null =True )#line:527
    updated_at =DateTimeField (null =True )#line:528
    class Meta :#line:530
        table_name ='card_awakening_sets'#line:531
class CardAwakenings (BaseModel ):#line:534
    awakening_item_id =IntegerField ()#line:535
    card_awakening_set_id =IntegerField (index =True ,null =True )#line:536
    created_at =DateTimeField (null =True )#line:537
    num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:538
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:539
    updated_at =DateTimeField (null =True )#line:540
    class Meta :#line:542
        table_name ='card_awakenings'#line:543
class CardCardCategories (BaseModel ):#line:546
    card_category_id =BigIntegerField (index =True )#line:547
    card_id =BigIntegerField ()#line:548
    created_at =DateTimeField ()#line:549
    id =BigAutoField ()#line:550
    num =IntegerField ()#line:551
    updated_at =DateTimeField ()#line:552
    class Meta :#line:554
        table_name ='card_card_categories'#line:555
        indexes =((('card_id','card_category_id'),False ),(('card_id','num'),False ),)#line:556
class CardCategories (BaseModel ):#line:559
    created_at =DateTimeField (null =True )#line:560
    name =CharField ()#line:561
    open_at =DateTimeField ()#line:562
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:563
    updated_at =DateTimeField (null =True )#line:564
    class Meta :#line:566
        table_name ='card_categories'#line:567
class CardExps (BaseModel ):#line:570
    created_at =DateTimeField (null =True )#line:571
    exp_total =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:572
    exp_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:573
    lv =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:574
    updated_at =DateTimeField (null =True )#line:575
    class Meta :#line:577
        table_name ='card_exps'#line:578
        indexes =((('exp_total','lv','exp_type'),False ),(('exp_type','exp_total'),False ),(('lv','exp_type'),False ),)#line:579
class CardGrowths (BaseModel ):#line:582
    coef =FloatField ()#line:583
    created_at =DateTimeField (null =True )#line:584
    grow_type =IntegerField ()#line:585
    lv =IntegerField ()#line:586
    updated_at =DateTimeField (null =True )#line:587
    class Meta :#line:589
        table_name ='card_growths'#line:590
        indexes =((('grow_type','lv'),False ),)#line:591
class CardMotions (BaseModel ):#line:594
    card_id =IntegerField ()#line:595
    category =IntegerField ()#line:596
    created_at =DateTimeField (null =True )#line:597
    filename =CharField (null =True )#line:598
    updated_at =DateTimeField (null =True )#line:599
    class Meta :#line:601
        table_name ='card_motions'#line:602
        indexes =((('card_id','category','filename'),False ),)#line:603
class CardSpecials (BaseModel ):#line:606
    bonus_view_id1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:607
    bonus_view_id2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:608
    card_id =IntegerField (index =True )#line:609
    created_at =DateTimeField (null =True )#line:610
    eball_num_start =IntegerField (constraints =[SQL ("DEFAULT '12'")])#line:611
    is_ultra_special =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:612
    lv_start =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:613
    special_bonus_id1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:614
    special_bonus_id2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:615
    special_bonus_lv1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:616
    special_bonus_lv2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:617
    special_id =IntegerField ()#line:618
    updated_at =DateTimeField (null =True )#line:619
    view_id =IntegerField ()#line:620
    class Meta :#line:622
        table_name ='card_specials'#line:623
class CardTrainingFieldExpUpProbs (BaseModel ):#line:626
    created_at =DateTimeField (null =True )#line:627
    effect =FloatField (constraints =[SQL ("DEFAULT '0'")])#line:628
    key =CharField (index =True )#line:629
    success_prob_percent =FloatField (constraints =[SQL ("DEFAULT '0'")])#line:630
    updated_at =DateTimeField (null =True )#line:631
    class Meta :#line:633
        table_name ='card_training_field_exp_up_probs'#line:634
class CardTrainingSkillLvUpProbs (BaseModel ):#line:637
    lr =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:638
    n =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:639
    r =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:640
    rarity =CharField (index =True )#line:641
    sr =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:642
    ssr =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:643
    ur =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:644
    class Meta :#line:646
        table_name ='card_training_skill_lv_up_probs'#line:647
class CardTrainingSkillLvs (BaseModel ):#line:650
    card_id =IntegerField (index =True )#line:651
    condition =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:652
    created_at =DateTimeField (null =True )#line:653
    probability =IntegerField (constraints =[SQL ("DEFAULT '100'")])#line:654
    skill_lv =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:655
    updated_at =DateTimeField (null =True )#line:656
    class Meta :#line:658
        table_name ='card_training_skill_lvs'#line:659
class CardUniqueInfos (BaseModel ):#line:662
    created_at =DateTimeField (null =True )#line:663
    kana =CharField (null =True )#line:664
    name =CharField ()#line:665
    updated_at =DateTimeField (null =True )#line:666
    class Meta :#line:668
        table_name ='card_unique_infos'#line:669
class Cards (BaseModel ):#line:672
    atk_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:673
    atk_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:674
    aura_id =IntegerField (null =True )#line:675
    aura_offset_x =IntegerField (null =True )#line:676
    aura_offset_y =IntegerField (null =True )#line:677
    aura_scale =FloatField (null =True )#line:678
    awaked_card_id =IntegerField (null =True )#line:679
    awakening_element_type =IntegerField (null =True )#line:680
    awakening_number =IntegerField (null =True )#line:681
    bg_effect_id =IntegerField (null =True )#line:682
    card_unique_info_id =IntegerField ()#line:683
    character_id =IntegerField ()#line:684
    collectable_type =IntegerField (null =True )#line:685
    cost =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:686
    created_at =DateTimeField (null =True )#line:687
    def_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:688
    def_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:689
    eball_mod_max =IntegerField ()#line:690
    eball_mod_max_num =IntegerField ()#line:691
    eball_mod_mid =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:692
    eball_mod_mid_num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:693
    eball_mod_min =IntegerField ()#line:694
    eball_mod_num100 =IntegerField ()#line:695
    element =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:696
    exp_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:697
    face_x =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:698
    face_y =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:699
    grow_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:700
    hp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:701
    hp_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:702
    is_aura_front =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:703
    is_selling_only =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:704
    leader_skill_id =IntegerField (null =True )#line:705
    link_skill1_id =IntegerField (null =True )#line:706
    link_skill2_id =IntegerField (null =True )#line:707
    link_skill3_id =IntegerField (null =True )#line:708
    link_skill4_id =IntegerField (null =True )#line:709
    link_skill5_id =IntegerField (null =True )#line:710
    link_skill6_id =IntegerField (null =True )#line:711
    link_skill7_id =IntegerField (null =True )#line:712
    lv_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:713
    max_level_reward_id =IntegerField (null =True )#line:714
    max_level_reward_type =CharField (null =True )#line:715
    name =CharField ()#line:716
    open_at =DateTimeField ()#line:717
    optimal_awakening_grow_type =IntegerField (null =True )#line:718
    passive_skill_set_id =IntegerField (null =True )#line:719
    potential_board_id =IntegerField (null =True )#line:720
    price =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:721
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:722
    resource_id =IntegerField (null =True )#line:723
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:724
    skill_id =IntegerField (null =True )#line:725
    skill_lv_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:726
    special_id =IntegerField (null =True )#line:727
    special_motion =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:728
    training_exp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:729
    updated_at =DateTimeField (null =True )#line:730
    class Meta :#line:732
        table_name ='cards'#line:733
class Characters (BaseModel ):#line:736
    created_at =DateTimeField (null =True )#line:737
    name =CharField ()#line:738
    race =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:739
    sex =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:740
    size =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:741
    updated_at =DateTimeField (null =True )#line:742
    class Meta :#line:744
        table_name ='characters'#line:745
class ClientSettings (BaseModel ):#line:748
    created_at =DateTimeField ()#line:749
    key =CharField (primary_key =True )#line:750
    updated_at =DateTimeField ()#line:751
    value =CharField ()#line:752
    class Meta :#line:754
        table_name ='client_settings'#line:755
class CollectionCards (BaseModel ):#line:758
    card_id =IntegerField ()#line:759
    collection_unique_id =IntegerField ()#line:760
    created_at =DateTimeField (null =True )#line:761
    event_id =IntegerField (null =True )#line:762
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:763
    updated_at =DateTimeField (null =True )#line:764
    class Meta :#line:766
        table_name ='collection_cards'#line:767
        indexes =((('collection_unique_id','card_id'),False ),)#line:768
class CollectionCategories (BaseModel ):#line:771
    created_at =DateTimeField (null =True )#line:772
    name =CharField ()#line:773
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:774
    updated_at =DateTimeField (null =True )#line:775
    class Meta :#line:777
        table_name ='collection_categories'#line:778
class CollectionUniques (BaseModel ):#line:781
    background_id =IntegerField ()#line:782
    card_id =IntegerField ()#line:783
    collection_category_id =IntegerField ()#line:784
    created_at =DateTimeField (null =True )#line:785
    name =CharField ()#line:786
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:787
    updated_at =DateTimeField (null =True )#line:788
    class Meta :#line:790
        table_name ='collection_uniques'#line:791
        indexes =((('collection_category_id','name'),False ),)#line:792
class EffectPacks (BaseModel ):#line:795
    alpha =IntegerField (constraints =[SQL ("DEFAULT '255'")])#line:796
    blue =IntegerField (constraints =[SQL ("DEFAULT '255'")])#line:797
    category =IntegerField ()#line:798
    created_at =DateTimeField (null =True )#line:799
    green =IntegerField (constraints =[SQL ("DEFAULT '255'")])#line:800
    name =CharField ()#line:801
    pack_name =CharField ()#line:802
    red =IntegerField (constraints =[SQL ("DEFAULT '255'")])#line:803
    scene_name =CharField ()#line:804
    updated_at =DateTimeField (null =True )#line:805
    class Meta :#line:807
        table_name ='effect_packs'#line:808
class EnemyAiConditions (BaseModel ):#line:811
    action_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:812
    ai_param =IntegerField (null =True )#line:813
    ai_param2 =IntegerField (null =True )#line:814
    ai_type =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:815
    atk_rate_1 =IntegerField (constraints =[SQL ("DEFAULT '100'")])#line:816
    atk_rate_2 =IntegerField (constraints =[SQL ("DEFAULT '100'")])#line:817
    created_at =DateTimeField (null =True )#line:818
    hp_rate_begin =FloatField (constraints =[SQL ("DEFAULT '0'")])#line:819
    hp_rate_end =FloatField (constraints =[SQL ("DEFAULT '0'")])#line:820
    max_num_per_turn =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:821
    max_number =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:822
    min_interval =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:823
    next_ai_type =IntegerField (null =True )#line:824
    recover_hp_rate =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:825
    updated_at =DateTimeField (null =True )#line:826
    weight =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:827
    class Meta :#line:829
        table_name ='enemy_ai_conditions'#line:830
class EnemySkills (BaseModel ):#line:833
    cau_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:834
    cau_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:835
    cau_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:836
    causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:837
    created_at =DateTimeField (null =True )#line:838
    description =CharField (null =True )#line:839
    eff_value1 =IntegerField (null =True )#line:840
    eff_value2 =IntegerField (null =True )#line:841
    eff_value3 =IntegerField (null =True )#line:842
    efficacy_type =IntegerField ()#line:843
    exec_timing_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:844
    icon_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:845
    name =CharField ()#line:846
    probability =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:847
    sub_target_type_set_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:848
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:849
    target_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:850
    target_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:851
    target_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:852
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:853
    updated_at =DateTimeField (null =True )#line:854
    class Meta :#line:856
        table_name ='enemy_skills'#line:857
class EventkagiItems (BaseModel ):#line:860
    area_tab_id =IntegerField ()#line:861
    created_at =DateTimeField (null =True )#line:862
    description =CharField ()#line:863
    name =CharField ()#line:864
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:865
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:866
    updated_at =DateTimeField (null =True )#line:867
    class Meta :#line:869
        table_name ='eventkagi_items'#line:870
class ForcedScripts (BaseModel ):#line:873
    created_at =DateTimeField (null =True )#line:874
    script_id =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:875
    updated_at =DateTimeField (null =True )#line:876
    class Meta :#line:878
        table_name ='forced_scripts'#line:879
class HelpBodies (BaseModel ):#line:882
    created_at =DateTimeField (null =True )#line:883
    description =TextField (null =True )#line:884
    help_id =IntegerField (index =True ,null =True )#line:885
    image =CharField (null =True )#line:886
    updated_at =DateTimeField (null =True )#line:887
    class Meta :#line:889
        table_name ='help_bodies'#line:890
class HelpCategories (BaseModel ):#line:893
    created_at =DateTimeField (null =True )#line:894
    num =IntegerField (null =True )#line:895
    title =CharField ()#line:896
    updated_at =DateTimeField (null =True )#line:897
    class Meta :#line:899
        table_name ='help_categories'#line:900
class Helps (BaseModel ):#line:903
    created_at =DateTimeField (null =True )#line:904
    description =TextField (null =True )#line:905
    help_category_id =IntegerField (index =True )#line:906
    num =IntegerField (null =True )#line:907
    title =CharField ()#line:908
    updated_at =DateTimeField (null =True )#line:909
    class Meta :#line:911
        table_name ='helps'#line:912
class LayoutPermissions (BaseModel ):#line:915
    created_at =DateTimeField (null =True )#line:916
    parts_name =CharField ()#line:917
    status =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:918
    updated_at =DateTimeField (null =True )#line:919
    class Meta :#line:921
        table_name ='layout_permissions'#line:922
class LeaderSkills (BaseModel ):#line:925
    calc_option1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:926
    calc_option2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:927
    calc_option3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:928
    calc_option4 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:929
    calc_option5 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:930
    cau_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:931
    cau_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:932
    cau_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:933
    causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:934
    created_at =DateTimeField (null =True )#line:935
    description =CharField ()#line:936
    eff1_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:937
    eff1_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:938
    eff1_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:939
    eff2_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:940
    eff2_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:941
    eff2_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:942
    eff3_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:943
    eff3_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:944
    eff3_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:945
    eff4_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:946
    eff4_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:947
    eff4_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:948
    eff5_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:949
    eff5_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:950
    eff5_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:951
    efficacy_type1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:952
    efficacy_type2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:953
    efficacy_type3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:954
    efficacy_type4 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:955
    efficacy_type5 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:956
    exec_timing_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:957
    name =CharField ()#line:958
    sub_target_type_set_id1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:959
    sub_target_type_set_id2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:960
    sub_target_type_set_id3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:961
    sub_target_type_set_id4 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:962
    sub_target_type_set_id5 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:963
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:964
    updated_at =DateTimeField (null =True )#line:965
    class Meta :#line:967
        table_name ='leader_skills'#line:968
class LevelBgs (BaseModel ):#line:971
    bg1_coef =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:972
    bg1_enable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:973
    bg1_flip_disable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:974
    bg2_coef =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:975
    bg2_enable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:976
    bg2_flip_disable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:977
    bg3_coef =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:978
    bg3_enable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:979
    bg3_flip_disable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:980
    bg4_coef =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:981
    bg4_enable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:982
    bg4_flip_disable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:983
    created_at =DateTimeField (null =True )#line:984
    name =CharField ()#line:985
    updated_at =DateTimeField (null =True )#line:986
    class Meta :#line:988
        table_name ='level_bgs'#line:989
class LinkSkills (BaseModel ):#line:992
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:993
    created_at =DateTimeField (null =True )#line:994
    description =CharField ()#line:995
    eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:996
    eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:997
    eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:998
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:999
    influence_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1000
    kana =CharField (null =True )#line:1001
    link_check_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1002
    lnk_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1003
    lnk_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1004
    lnk_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1005
    name =CharField ()#line:1006
    need_link_num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1007
    sub_target_type_set_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1008
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1009
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1010
    updated_at =DateTimeField (null =True )#line:1011
    class Meta :#line:1013
        table_name ='link_skills'#line:1014
class Marquees (BaseModel ):#line:1017
    created_at =DateTimeField (null =True )#line:1018
    description =TextField ()#line:1019
    scene_name =CharField ()#line:1020
    updated_at =DateTimeField (null =True )#line:1021
    class Meta :#line:1023
        table_name ='marquees'#line:1024
class MissionBeginnersGuides (BaseModel ):#line:1027
    banner_image =CharField (null =True )#line:1028
    beginners_guide_id =IntegerField ()#line:1029
    created_at =DateTimeField (null =True )#line:1030
    description_image =CharField (null =True )#line:1031
    description_script_id =IntegerField (null =True )#line:1032
    next_mission_id =IntegerField ()#line:1033
    updated_at =DateTimeField (null =True )#line:1034
    class Meta :#line:1036
        table_name ='mission_beginners_guides'#line:1037
class MissionCampaigns (BaseModel ):#line:1040
    campaign_id =IntegerField ()#line:1041
    created_at =DateTimeField (null =True )#line:1042
    mission_id =IntegerField (index =True )#line:1043
    name =CharField ()#line:1044
    updated_at =DateTimeField (null =True )#line:1045
    class Meta :#line:1047
        table_name ='mission_campaigns'#line:1048
class MissionCategories (BaseModel ):#line:1051
    created_at =DateTimeField (null =True )#line:1052
    dragonball_session_id =IntegerField (null =True )#line:1053
    name =CharField ()#line:1054
    required_rank =IntegerField (null =True )#line:1055
    type =CharField (null =True )#line:1056
    updated_at =DateTimeField (null =True )#line:1057
    class Meta :#line:1059
        table_name ='mission_categories'#line:1060
class MissionPeriods (BaseModel ):#line:1063
    created_at =DateTimeField (null =True )#line:1064
    mission_id =IntegerField (index =True )#line:1065
    type =CharField (null =True )#line:1066
    updated_at =DateTimeField (null =True )#line:1067
    wday =IntegerField (null =True )#line:1068
    wday_hours_to_end =IntegerField (null =True )#line:1069
    wday_start_at =TimeField (null =True )#line:1070
    class Meta :#line:1072
        table_name ='mission_periods'#line:1073
class MissionRewards (BaseModel ):#line:1076
    announcement_label =CharField (null =True )#line:1077
    announcement_priority =IntegerField (null =True )#line:1078
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1079
    created_at =DateTimeField (null =True )#line:1080
    item_id =IntegerField ()#line:1081
    item_type =CharField ()#line:1082
    mission_id =IntegerField (index =True )#line:1083
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1084
    updated_at =DateTimeField (null =True )#line:1085
    class Meta :#line:1087
        table_name ='mission_rewards'#line:1088
class Missions (BaseModel ):#line:1091
    area_id =IntegerField (index =True ,null =True )#line:1092
    conditions =TextField (null =True )#line:1093
    created_at =DateTimeField (null =True )#line:1094
    description =TextField ()#line:1095
    end_at =DateTimeField ()#line:1096
    end_at_hidden =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1097
    mission_category_id =IntegerField (index =True )#line:1098
    name =CharField ()#line:1099
    orderer_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1100
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1101
    start_at =DateTimeField ()#line:1102
    target_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1103
    type =CharField (null =True )#line:1104
    updated_at =DateTimeField (null =True )#line:1105
    z_battle_stage_id =IntegerField (index =True ,null =True )#line:1106
    class Meta :#line:1108
        table_name ='missions'#line:1109
        indexes =((('type','start_at','end_at'),False ),)#line:1110
class OptimalAwakeningGrowths (BaseModel ):#line:1113
    leader_skill_id =IntegerField (null =True )#line:1114
    lv_max =IntegerField ()#line:1115
    optimal_awakening_grow_type =IntegerField ()#line:1116
    passive_skill_set_id =IntegerField (null =True )#line:1117
    skill_lv_max =IntegerField ()#line:1118
    step =IntegerField ()#line:1119
    class Meta :#line:1121
        table_name ='optimal_awakening_growths'#line:1122
        indexes =((('optimal_awakening_grow_type','step'),False ),)#line:1123
class PassiveSkillSetRelations (BaseModel ):#line:1126
    created_at =DateTimeField (null =True )#line:1127
    passive_skill_id =IntegerField ()#line:1128
    passive_skill_set_id =IntegerField (index =True )#line:1129
    updated_at =DateTimeField (null =True )#line:1130
    class Meta :#line:1132
        table_name ='passive_skill_set_relations'#line:1133
class PassiveSkillSets (BaseModel ):#line:1136
    created_at =DateTimeField (null =True )#line:1137
    description =CharField (null =True )#line:1138
    name =CharField (null =True )#line:1139
    updated_at =DateTimeField (null =True )#line:1140
    class Meta :#line:1142
        table_name ='passive_skill_sets'#line:1143
class PassiveSkills (BaseModel ):#line:1146
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1147
    cau_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1148
    cau_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1149
    cau_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1150
    causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1151
    created_at =DateTimeField (null =True )#line:1152
    description =CharField ()#line:1153
    eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1154
    eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1155
    eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1156
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1157
    exec_timing_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1158
    influence_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1159
    is_once =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1160
    name =CharField ()#line:1161
    probability =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1162
    sub_target_type_set_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1163
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1164
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1165
    updated_at =DateTimeField (null =True )#line:1166
    class Meta :#line:1168
        table_name ='passive_skills'#line:1169
class Points (BaseModel ):#line:1172
    amount =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1173
    created_at =DateTimeField (null =True )#line:1174
    type =CharField (null =True )#line:1175
    updated_at =DateTimeField (null =True )#line:1176
    class Meta :#line:1178
        table_name ='points'#line:1179
class PotentialBoards (BaseModel ):#line:1182
    comment =CharField (null =True )#line:1183
    created_at =DateTimeField (null =True )#line:1184
    updated_at =DateTimeField (null =True )#line:1185
    class Meta :#line:1187
        table_name ='potential_boards'#line:1188
class PotentialEventSelectionTables (BaseModel ):#line:1191
    comment =CharField (null =True )#line:1192
    created_at =DateTimeField (null =True )#line:1193
    required_stone_for_unrelease =IntegerField ()#line:1194
    updated_at =DateTimeField (null =True )#line:1195
    class Meta :#line:1197
        table_name ='potential_event_selection_tables'#line:1198
class PotentialEventSelections (BaseModel ):#line:1201
    created_at =DateTimeField (null =True )#line:1202
    event_id =IntegerField ()#line:1203
    selection_table_id =IntegerField ()#line:1204
    updated_at =DateTimeField (null =True )#line:1205
    class Meta :#line:1207
        table_name ='potential_event_selections'#line:1208
class PotentialEvents (BaseModel ):#line:1211
    additional_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1212
    created_at =DateTimeField (null =True )#line:1213
    currency_id =IntegerField (null =True )#line:1214
    type =CharField ()#line:1215
    updated_at =DateTimeField (null =True )#line:1216
    class Meta :#line:1218
        table_name ='potential_events'#line:1219
class PotentialItems (BaseModel ):#line:1222
    created_at =DateTimeField (null =True )#line:1223
    description =CharField ()#line:1224
    name =CharField ()#line:1225
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1226
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1227
    updated_at =DateTimeField (null =True )#line:1228
    class Meta :#line:1230
        table_name ='potential_items'#line:1231
class PotentialSkillLvValues (BaseModel ):#line:1234
    created_at =DateTimeField (null =True )#line:1235
    lv =IntegerField ()#line:1236
    potential_skill_id =IntegerField ()#line:1237
    updated_at =DateTimeField (null =True )#line:1238
    value =IntegerField ()#line:1239
    class Meta :#line:1241
        table_name ='potential_skill_lv_values'#line:1242
        indexes =((('potential_skill_id','lv'),False ),)#line:1243
class PotentialSkills (BaseModel ):#line:1246
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1247
    cau_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1248
    cau_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1249
    cau_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1250
    causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1251
    created_at =DateTimeField (null =True )#line:1252
    description =CharField ()#line:1253
    eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1254
    eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1255
    eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1256
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1257
    exec_timing_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1258
    influence_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1259
    is_once =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1260
    name =CharField ()#line:1261
    probability =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1262
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1263
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1264
    updated_at =DateTimeField (null =True )#line:1265
    variable_column =CharField (constraints =[SQL ("DEFAULT 'eff_value1'")])#line:1266
    class Meta :#line:1268
        table_name ='potential_skills'#line:1269
class PotentialSquareConditionSetRelations (BaseModel ):#line:1272
    condition_id =IntegerField ()#line:1273
    condition_set_id =IntegerField ()#line:1274
    created_at =DateTimeField (null =True )#line:1275
    updated_at =DateTimeField (null =True )#line:1276
    class Meta :#line:1278
        table_name ='potential_square_condition_set_relations'#line:1279
class PotentialSquareConditionSets (BaseModel ):#line:1282
    comment =CharField (null =True )#line:1283
    created_at =DateTimeField (null =True )#line:1284
    updated_at =DateTimeField (null =True )#line:1285
    class Meta :#line:1287
        table_name ='potential_square_condition_sets'#line:1288
class PotentialSquareConditions (BaseModel ):#line:1291
    comment =CharField (null =True )#line:1292
    conditions =TextField (null =True )#line:1293
    created_at =DateTimeField (null =True )#line:1294
    type =CharField ()#line:1295
    updated_at =DateTimeField (null =True )#line:1296
    class Meta :#line:1298
        table_name ='potential_square_conditions'#line:1299
class PotentialSquareRelations (BaseModel ):#line:1302
    created_at =DateTimeField (null =True )#line:1303
    potential_square_id =IntegerField (index =True )#line:1304
    prev_potential_square_id =IntegerField (null =True )#line:1305
    updated_at =DateTimeField (null =True )#line:1306
    class Meta :#line:1308
        table_name ='potential_square_relations'#line:1309
class PotentialSquares (BaseModel ):#line:1312
    condition_set_id =IntegerField ()#line:1313
    created_at =DateTimeField (null =True )#line:1314
    event_id =IntegerField ()#line:1315
    is_locked =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1316
    potential_board_id =IntegerField ()#line:1317
    route =IntegerField (null =True )#line:1318
    updated_at =DateTimeField (null =True )#line:1319
    class Meta :#line:1321
        table_name ='potential_squares'#line:1322
class QuestCategoryBonusGroups (BaseModel ):#line:1325
    created_at =DateTimeField (null =True )#line:1326
    description =TextField (null =True )#line:1327
    name =CharField ()#line:1328
    quest_category_bonus_type =CharField (index =True )#line:1329
    updated_at =DateTimeField (null =True )#line:1330
    class Meta :#line:1332
        table_name ='quest_category_bonus_groups'#line:1333
class QuestCategoryBonusRarityTables (BaseModel ):#line:1336
    created_at =DateTimeField (null =True )#line:1337
    description =CharField ()#line:1338
    rarity_lr =IntegerField ()#line:1339
    rarity_n =IntegerField ()#line:1340
    rarity_r =IntegerField ()#line:1341
    rarity_sr =IntegerField ()#line:1342
    rarity_ssr =IntegerField ()#line:1343
    rarity_ur =IntegerField ()#line:1344
    updated_at =DateTimeField (null =True )#line:1345
    class Meta :#line:1347
        table_name ='quest_category_bonus_rarity_tables'#line:1348
class QuestCategoryBonuses (BaseModel ):#line:1351
    card_category_id =IntegerField ()#line:1352
    created_at =DateTimeField (null =True )#line:1353
    quest_category_bonus_rarity_table_id =IntegerField (null =True )#line:1354
    quest_id =IntegerField (index =True )#line:1355
    type =CharField ()#line:1356
    updated_at =DateTimeField (null =True )#line:1357
    class Meta :#line:1359
        table_name ='quest_category_bonuses'#line:1360
class Quests (BaseModel ):#line:1363
    all_clear_bonus_stones =IntegerField (null =True )#line:1364
    any_clear_bonus_stones =IntegerField (null =True )#line:1365
    area_id =IntegerField (index =True )#line:1366
    boostable =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1367
    can_ignore_difficulty_order =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1368
    created_at =DateTimeField (null =True )#line:1369
    icon_x =IntegerField (null =True )#line:1370
    icon_y =IntegerField (null =True )#line:1371
    interval_reset_visited_days =IntegerField (null =True )#line:1372
    name =CharField ()#line:1373
    prev_quest_id =IntegerField (index =True ,null =True )#line:1374
    start_at =DateTimeField ()#line:1375
    updated_at =DateTimeField (null =True )#line:1376
    visit_count_max =IntegerField (null =True )#line:1377
    class Meta :#line:1379
        table_name ='quests'#line:1380
        indexes =((('area_id','prev_quest_id'),False ),)#line:1381
class RankStatuses (BaseModel ):#line:1384
    act_max =IntegerField ()#line:1385
    created_at =DateTimeField (null =True )#line:1386
    exp_total =IntegerField (index =True )#line:1387
    friends_capacity =IntegerField ()#line:1388
    rank =IntegerField (index =True )#line:1389
    team_cost_capacity =IntegerField ()#line:1390
    updated_at =DateTimeField (null =True )#line:1391
    class Meta :#line:1393
        table_name ='rank_statuses'#line:1394
class RecommendSpecialViews (BaseModel ):#line:1397
    card_id =BigIntegerField (index =True )#line:1398
    created_at =DateTimeField ()#line:1399
    id =BigAutoField ()#line:1400
    updated_at =DateTimeField ()#line:1401
    view_id =IntegerField ()#line:1402
    class Meta :#line:1404
        table_name ='recommend_special_views'#line:1405
class RelatedCardCategories (BaseModel ):#line:1408
    card_category_id =IntegerField ()#line:1409
    created_at =DateTimeField (null =True )#line:1410
    enemy_skill_id =IntegerField ()#line:1411
    updated_at =DateTimeField (null =True )#line:1412
    class Meta :#line:1414
        table_name ='related_card_categories'#line:1415
class RelatedLinkSkills (BaseModel ):#line:1418
    created_at =DateTimeField (null =True )#line:1419
    enemy_skill_id =IntegerField ()#line:1420
    link_skill_id =IntegerField ()#line:1421
    updated_at =DateTimeField (null =True )#line:1422
    class Meta :#line:1424
        table_name ='related_link_skills'#line:1425
        indexes =((('enemy_skill_id','link_skill_id'),False ),)#line:1426
class RelatedPassiveSkillSets (BaseModel ):#line:1429
    created_at =DateTimeField (null =True )#line:1430
    enemy_skill_id =IntegerField ()#line:1431
    passive_skill_set_id =IntegerField ()#line:1432
    updated_at =DateTimeField (null =True )#line:1433
    class Meta :#line:1435
        table_name ='related_passive_skill_sets'#line:1436
        indexes =((('enemy_skill_id','passive_skill_set_id'),False ),)#line:1437
class RmbattleBgmPatterns (BaseModel ):#line:1440
    boss_bgm_id =IntegerField ()#line:1441
    created_at =DateTimeField (null =True )#line:1442
    last_boss_bgm_id =IntegerField ()#line:1443
    normal_bgm_id =IntegerField ()#line:1444
    updated_at =DateTimeField (null =True )#line:1445
    class Meta :#line:1447
        table_name ='rmbattle_bgm_patterns'#line:1448
class RmbattleHelpBodies (BaseModel ):#line:1451
    created_at =DateTimeField (null =True )#line:1452
    description =CharField (null =True )#line:1453
    image =CharField (null =True )#line:1454
    rmbattle_help_id =IntegerField (index =True )#line:1455
    updated_at =DateTimeField (null =True )#line:1456
    class Meta :#line:1458
        table_name ='rmbattle_help_bodies'#line:1459
class RmbattleHelpCategories (BaseModel ):#line:1462
    created_at =DateTimeField (null =True )#line:1463
    num =IntegerField (null =True )#line:1464
    title =CharField ()#line:1465
    updated_at =DateTimeField (null =True )#line:1466
    class Meta :#line:1468
        table_name ='rmbattle_help_categories'#line:1469
class RmbattleHelps (BaseModel ):#line:1472
    created_at =DateTimeField (null =True )#line:1473
    description =TextField (null =True )#line:1474
    num =IntegerField (null =True )#line:1475
    rmbattle_help_category_id =IntegerField (index =True )#line:1476
    title =CharField ()#line:1477
    updated_at =DateTimeField (null =True )#line:1478
    class Meta :#line:1480
        table_name ='rmbattle_helps'#line:1481
class RmbattleMissionRewards (BaseModel ):#line:1484
    card_exp_init =IntegerField ()#line:1485
    created_at =DateTimeField (null =True )#line:1486
    description =CharField ()#line:1487
    gift_description =CharField ()#line:1488
    item_id =IntegerField ()#line:1489
    item_type =CharField ()#line:1490
    quantity =IntegerField ()#line:1491
    rmbattle_mission_id =IntegerField (index =True )#line:1492
    updated_at =DateTimeField (null =True )#line:1493
    class Meta :#line:1495
        table_name ='rmbattle_mission_rewards'#line:1496
class RmbattleMissions (BaseModel ):#line:1499
    conditions =TextField ()#line:1500
    created_at =DateTimeField (null =True )#line:1501
    is_attention =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1502
    name =CharField ()#line:1503
    priority =IntegerField ()#line:1504
    rmbattle_id =IntegerField ()#line:1505
    target_value =IntegerField (null =True )#line:1506
    type =CharField ()#line:1507
    updated_at =DateTimeField (null =True )#line:1508
    class Meta :#line:1510
        table_name ='rmbattle_missions'#line:1511
        indexes =((('rmbattle_id','type'),False ),)#line:1512
class Shops (BaseModel ):#line:1515
    close_at =DateTimeField ()#line:1516
    created_at =DateTimeField (null =True )#line:1517
    end_at =DateTimeField ()#line:1518
    item_change_interval_sec =IntegerField (null =True )#line:1519
    open_at =DateTimeField ()#line:1520
    required_stone_to_change_item =IntegerField (null =True )#line:1521
    start_at =DateTimeField ()#line:1522
    type =CharField (null =True )#line:1523
    updated_at =DateTimeField (null =True )#line:1524
    class Meta :#line:1526
        table_name ='shops'#line:1527
class SkillCausalities (BaseModel ):#line:1530
    cau_val1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1531
    cau_val2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1532
    cau_val3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1533
    causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1534
    created_at =DateTimeField ()#line:1535
    id =BigAutoField ()#line:1536
    skill_causality_set_id =IntegerField (index =True )#line:1537
    updated_at =DateTimeField ()#line:1538
    class Meta :#line:1540
        table_name ='skill_causalities'#line:1541
class SkillGroupRelations (BaseModel ):#line:1544
    created_at =DateTimeField ()#line:1545
    skill_group_id =BigIntegerField ()#line:1546
    target_id =BigIntegerField ()#line:1547
    target_type =CharField ()#line:1548
    updated_at =DateTimeField ()#line:1549
    class Meta :#line:1551
        table_name ='skill_group_relations'#line:1552
        indexes =((('target_type','target_id','skill_group_id'),False ),)#line:1553
        primary_key =False #line:1554
class SkillGroups (BaseModel ):#line:1557
    created_at =DateTimeField ()#line:1558
    id =BigAutoField ()#line:1559
    name =CharField ()#line:1560
    priority =IntegerField ()#line:1561
    updated_at =DateTimeField ()#line:1562
    class Meta :#line:1564
        table_name ='skill_groups'#line:1565
class SkillLabels (BaseModel ):#line:1568
    created_at =DateTimeField (null =True )#line:1569
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1570
    is_display =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1571
    updated_at =DateTimeField (null =True )#line:1572
    class Meta :#line:1574
        table_name ='skill_labels'#line:1575
class Skills (BaseModel ):#line:1578
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1579
    created_at =DateTimeField (null =True )#line:1580
    description =CharField ()#line:1581
    eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1582
    eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1583
    eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1584
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1585
    influence_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1586
    name =CharField ()#line:1587
    need_turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1588
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1589
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1590
    updated_at =DateTimeField (null =True )#line:1591
    class Meta :#line:1593
        table_name ='skills'#line:1594
class SoundEffectOffsets (BaseModel ):#line:1597
    created_at =DateTimeField (null =True )#line:1598
    sound_effect_id =IntegerField ()#line:1599
    sound_effect_set_id =IntegerField (index =True )#line:1600
    start_offset_millisecond =IntegerField ()#line:1601
    updated_at =DateTimeField (null =True )#line:1602
    class Meta :#line:1604
        table_name ='sound_effect_offsets'#line:1605
class SpecialBonuses (BaseModel ):#line:1608
    calc_option =IntegerField (null =True )#line:1609
    cau_value1 =IntegerField (null =True )#line:1610
    cau_value2 =IntegerField (null =True )#line:1611
    cau_value3 =IntegerField (null =True )#line:1612
    causality_type =IntegerField (null =True )#line:1613
    created_at =DateTimeField (null =True )#line:1614
    description =CharField (null =True )#line:1615
    eff_value1 =IntegerField (null =True )#line:1616
    eff_value2 =IntegerField (null =True )#line:1617
    eff_value3 =IntegerField (null =True )#line:1618
    efficacy_type =IntegerField (null =True )#line:1619
    influence_type =IntegerField (null =True )#line:1620
    name =CharField (null =True )#line:1621
    probability =IntegerField (null =True )#line:1622
    target_type =IntegerField (null =True )#line:1623
    turn =IntegerField (null =True )#line:1624
    updated_at =DateTimeField (null =True )#line:1625
    class Meta :#line:1627
        table_name ='special_bonuses'#line:1628
class SpecialItems (BaseModel ):#line:1631
    created_at =DateTimeField (null =True )#line:1632
    description =TextField (null =True )#line:1633
    name =CharField (null =True )#line:1634
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1635
    updated_at =DateTimeField (null =True )#line:1636
    class Meta :#line:1638
        table_name ='special_items'#line:1639
class SpecialScripts (BaseModel ):#line:1642
    attack_attributes =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1643
    energy_color =IntegerField (null =True )#line:1644
    script_name =CharField (index =True )#line:1645
    class Meta :#line:1647
        table_name ='special_scripts'#line:1648
class SpecialViews (BaseModel ):#line:1651
    created_at =DateTimeField (null =True )#line:1652
    cut_in_card_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1653
    script_name =CharField ()#line:1654
    special_motion =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1655
    special_name_no =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1656
    updated_at =DateTimeField (null =True )#line:1657
    class Meta :#line:1659
        table_name ='special_views'#line:1660
class Specials (BaseModel ):#line:1663
    additional_effect =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1664
    aim_target =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1665
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1666
    check_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1667
    created_at =DateTimeField (null =True )#line:1668
    description =CharField ()#line:1669
    eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1670
    eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1671
    eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1672
    efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1673
    ex_cau_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1674
    ex_cau_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1675
    ex_cau_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1676
    ex_causality_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1677
    ex_eff_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1678
    ex_eff_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1679
    ex_eff_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1680
    ex_efficacy_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1681
    increase_rate =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1682
    influence_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1683
    lv_bonus =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1684
    lv_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1685
    lv_max =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1686
    name =CharField ()#line:1687
    prob =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1688
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1689
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1690
    updated_at =DateTimeField (null =True )#line:1691
    class Meta :#line:1693
        table_name ='specials'#line:1694
class StatusExtensions (BaseModel ):#line:1697
    amount =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1698
    created_at =DateTimeField (null =True )#line:1699
    type =CharField (null =True )#line:1700
    updated_at =DateTimeField (null =True )#line:1701
    class Meta :#line:1703
        table_name ='status_extensions'#line:1704
class SubTargetTypeSets (BaseModel ):#line:1707
    created_at =DateTimeField (null =True )#line:1708
    updated_at =DateTimeField (null =True )#line:1709
    class Meta :#line:1711
        table_name ='sub_target_type_sets'#line:1712
class SubTargetTypes (BaseModel ):#line:1715
    created_at =DateTimeField (null =True )#line:1716
    sub_target_type_set_id =IntegerField (index =True )#line:1717
    target_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1718
    target_value_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1719
    updated_at =DateTimeField (null =True )#line:1720
    class Meta :#line:1722
        table_name ='sub_target_types'#line:1723
class SugorokuMapPuzzleColors (BaseModel ):#line:1726
    created_at =DateTimeField (null =True )#line:1727
    updated_at =DateTimeField (null =True )#line:1728
    weight_blue =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1729
    weight_green =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1730
    weight_purple =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1731
    weight_rainbow =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1732
    weight_red =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1733
    weight_yellow =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1734
    class Meta :#line:1736
        table_name ='sugoroku_map_puzzle_colors'#line:1737
class SugorokuMaps (BaseModel ):#line:1740
    act =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1741
    battle_background_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1742
    battle_bgm_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1743
    boss_bgm_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1744
    clear_count_max =IntegerField (null =True )#line:1745
    created_at =DateTimeField (null =True )#line:1746
    danger_line_hp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1747
    dice_id =IntegerField (null =True )#line:1748
    difficulty =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1749
    eventkagi_num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1750
    finish_script_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1751
    first_focus_step =IntegerField (null =True )#line:1752
    is_cpu_only =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1753
    quest_id =IntegerField (null =True )#line:1754
    start_script_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1755
    sugoroku_bgm_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1756
    sugoroku_map_puzzle_color_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1757
    updated_at =DateTimeField (null =True )#line:1758
    user_exp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1759
    zeni =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1760
    class Meta :#line:1762
        table_name ='sugoroku_maps'#line:1763
        indexes =((('quest_id','difficulty'),False ),)#line:1764
class SupportItems (BaseModel ):#line:1767
    calc_option =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1768
    created_at =DateTimeField (null =True )#line:1769
    description =CharField ()#line:1770
    eff1_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1771
    eff1_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1772
    eff1_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1773
    eff2_value1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1774
    eff2_value2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1775
    eff2_value3 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1776
    efficacy_type1 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1777
    efficacy_type2 =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1778
    ingame_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1779
    max_per_quest =IntegerField (null =True )#line:1780
    max_per_quest_extended =IntegerField (null =True )#line:1781
    name =CharField (null =True )#line:1782
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1783
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1784
    target_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1785
    turn =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1786
    updated_at =DateTimeField (null =True )#line:1787
    class Meta :#line:1789
        table_name ='support_items'#line:1790
class Tips (BaseModel ):#line:1793
    created_at =DateTimeField (null =True )#line:1794
    description =TextField ()#line:1795
    end_at =DateTimeField (constraints =[SQL ("DEFAULT '2030-01-01 00:00:00'")])#line:1796
    image_name =CharField (null =True )#line:1797
    start_at =DateTimeField (constraints =[SQL ("DEFAULT '2000-01-01 00:00:00'")])#line:1798
    title =CharField ()#line:1799
    updated_at =DateTimeField (null =True )#line:1800
    weight =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1801
    class Meta :#line:1803
        table_name ='tips'#line:1804
class TitleScreens (BaseModel ):#line:1807
    bg_anime =CharField (null =True )#line:1808
    bgm_id =IntegerField (null =True )#line:1809
    chara_anime =CharField (null =True )#line:1810
    created_at =DateTimeField (null =True )#line:1811
    end_at =DateTimeField ()#line:1812
    start_at =DateTimeField ()#line:1813
    updated_at =DateTimeField (null =True )#line:1814
    class Meta :#line:1816
        table_name ='title_screens'#line:1817
class TrainingFields (BaseModel ):#line:1820
    addend =IntegerField (null =True )#line:1821
    card_training_field_exp_up_prob_id =IntegerField (null =True )#line:1822
    created_at =DateTimeField (null =True )#line:1823
    description =CharField ()#line:1824
    elements =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1825
    exp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1826
    level_bg_id =IntegerField ()#line:1827
    multiplier =FloatField (null =True )#line:1828
    name =CharField ()#line:1829
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1830
    updated_at =DateTimeField (null =True )#line:1831
    zeni =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1832
    class Meta :#line:1834
        table_name ='training_fields'#line:1835
class TrainingItems (BaseModel ):#line:1838
    created_at =DateTimeField (null =True )#line:1839
    description =CharField ()#line:1840
    element =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1841
    exp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1842
    name =CharField ()#line:1843
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1844
    selling_exchange_point =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1845
    updated_at =DateTimeField (null =True )#line:1846
    zeni_to_use =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1847
    class Meta :#line:1849
        table_name ='training_items'#line:1850
class TransformationDescriptions (BaseModel ):#line:1853
    created_at =DateTimeField (null =True )#line:1854
    description =CharField ()#line:1855
    skill_id =IntegerField ()#line:1856
    skill_type =CharField (constraints =[SQL ("DEFAULT ''")])#line:1857
    updated_at =DateTimeField (null =True )#line:1858
    class Meta :#line:1860
        table_name ='transformation_descriptions'#line:1861
        indexes =((('skill_type','skill_id'),False ),)#line:1862
class TreasureItems (BaseModel ):#line:1865
    created_at =DateTimeField (null =True )#line:1866
    description =CharField ()#line:1867
    image_suffix_number =IntegerField ()#line:1868
    name =CharField ()#line:1869
    rarity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1870
    updated_at =DateTimeField (null =True )#line:1871
    class Meta :#line:1873
        table_name ='treasure_items'#line:1874
class UltimateSpecials (BaseModel ):#line:1877
    created_at =DateTimeField ()#line:1878
    description =CharField ()#line:1879
    id =BigAutoField ()#line:1880
    increase_rate =IntegerField ()#line:1881
    name =CharField ()#line:1882
    updated_at =DateTimeField ()#line:1883
    class Meta :#line:1885
        table_name ='ultimate_specials'#line:1886
class WallpaperItems (BaseModel ):#line:1889
    created_at =DateTimeField ()#line:1890
    description =CharField (null =True )#line:1891
    name =CharField (null =True )#line:1892
    updated_at =DateTimeField ()#line:1893
    class Meta :#line:1895
        table_name ='wallpaper_items'#line:1896
class Worlds (BaseModel ):#line:1899
    bgm_id =IntegerField (null =True )#line:1900
    created_at =DateTimeField (null =True )#line:1901
    height =IntegerField (null =True )#line:1902
    layer0 =CharField (null =True )#line:1903
    layer1 =CharField (null =True )#line:1904
    layer2 =CharField (null =True )#line:1905
    layer3 =CharField (null =True )#line:1906
    name =CharField ()#line:1907
    prev_world_id =IntegerField (null =True )#line:1908
    split =IntegerField (null =True )#line:1909
    updated_at =DateTimeField (null =True )#line:1910
    width =IntegerField (null =True )#line:1911
    class Meta :#line:1913
        table_name ='worlds'#line:1914
class ZBattleCheckPoints (BaseModel ):#line:1917
    act =IntegerField ()#line:1918
    created_at =DateTimeField (null =True )#line:1919
    eventkagi_num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1920
    level =IntegerField ()#line:1921
    main_reward_id =IntegerField (null =True )#line:1922
    updated_at =DateTimeField (null =True )#line:1923
    z_battle_normal_reward_table_group_id =IntegerField ()#line:1924
    z_battle_stage_id =IntegerField (index =True )#line:1925
    class Meta :#line:1927
        table_name ='z_battle_check_points'#line:1928
        indexes =((('z_battle_stage_id','level'),False ),)#line:1929
class ZBattleEnemies (BaseModel ):#line:1932
    attack_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1933
    base_attack =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1934
    base_defence =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1935
    base_hp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1936
    card_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1937
    created_at =DateTimeField (null =True )#line:1938
    defence_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1939
    end_level =IntegerField (null =True )#line:1940
    hp_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1941
    ordinal_num =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1942
    performance_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1943
    skill_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1944
    special_attack_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1945
    start_level =IntegerField (constraints =[SQL ("DEFAULT '1'")])#line:1946
    updated_at =DateTimeField (null =True )#line:1947
    z_battle_stage_id =IntegerField (index =True ,null =True )#line:1948
    class Meta :#line:1950
        table_name ='z_battle_enemies'#line:1951
class ZBattleEnemyCardEscalations (BaseModel ):#line:1954
    card_id =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1955
    created_at =DateTimeField (null =True )#line:1956
    escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:1957
    level =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1958
    updated_at =DateTimeField (null =True )#line:1959
    class Meta :#line:1961
        table_name ='z_battle_enemy_card_escalations'#line:1962
class ZBattleEnemySkillEscalations (BaseModel ):#line:1965
    created_at =DateTimeField (null =True )#line:1966
    enemy_skill_id =IntegerField (null =True )#line:1967
    escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:1968
    level =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1969
    updated_at =DateTimeField (null =True )#line:1970
    class Meta :#line:1972
        table_name ='z_battle_enemy_skill_escalations'#line:1973
class ZBattleEnemyStatusEscalations (BaseModel ):#line:1976
    created_at =DateTimeField (null =True )#line:1977
    escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")],index =True )#line:1978
    escalation_value =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1979
    level =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:1980
    updated_at =DateTimeField (null =True )#line:1981
    class Meta :#line:1983
        table_name ='z_battle_enemy_status_escalations'#line:1984
class ZBattleFirstRewardLevelRanges (BaseModel ):#line:1987
    created_at =DateTimeField (null =True )#line:1988
    level =IntegerField ()#line:1989
    main_reward_id =IntegerField (null =True )#line:1990
    updated_at =DateTimeField (null =True )#line:1991
    z_battle_first_reward_set_id =IntegerField ()#line:1992
    z_battle_stage_id =IntegerField ()#line:1993
    class Meta :#line:1995
        table_name ='z_battle_first_reward_level_ranges'#line:1996
        indexes =((('z_battle_stage_id','level'),False ),)#line:1997
class ZBattleFirstRewards (BaseModel ):#line:2000
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2001
    created_at =DateTimeField (null =True )#line:2002
    item_id =IntegerField ()#line:2003
    item_type =CharField ()#line:2004
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2005
    updated_at =DateTimeField (null =True )#line:2006
    z_battle_first_reward_set_id =IntegerField (index =True )#line:2007
    class Meta :#line:2009
        table_name ='z_battle_first_rewards'#line:2010
class ZBattleNormalRewardTables (BaseModel ):#line:2013
    created_at =DateTimeField (null =True )#line:2014
    updated_at =DateTimeField (null =True )#line:2015
    z_battle_normal_reward_table_group_id =IntegerField (index =True )#line:2016
    class Meta :#line:2018
        table_name ='z_battle_normal_reward_tables'#line:2019
class ZBattleNormalRewards (BaseModel ):#line:2022
    card_exp_init =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2023
    created_at =DateTimeField (null =True )#line:2024
    item_id =IntegerField ()#line:2025
    item_type =CharField ()#line:2026
    quantity =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2027
    updated_at =DateTimeField (null =True )#line:2028
    z_battle_normal_reward_table_id =IntegerField (index =True )#line:2029
    class Meta :#line:2031
        table_name ='z_battle_normal_rewards'#line:2032
class ZBattlePowerupThresholds (BaseModel ):#line:2035
    atk =IntegerField (null =True )#line:2036
    created_at =DateTimeField (null =True )#line:2037
    def_ =IntegerField (column_name ='def',null =True )#line:2038
    hp =IntegerField (null =True )#line:2039
    special_atk =IntegerField (null =True )#line:2040
    updated_at =DateTimeField (null =True )#line:2041
    z_battle_stage_id =IntegerField (index =True )#line:2042
    class Meta :#line:2044
        table_name ='z_battle_powerup_thresholds'#line:2045
class ZBattlePowerupViews (BaseModel ):#line:2048
    created_at =DateTimeField (null =True )#line:2049
    enemy_skill_efficacy_type =IntegerField (index =True )#line:2050
    texture_name =CharField ()#line:2051
    updated_at =DateTimeField (null =True )#line:2052
    class Meta :#line:2054
        table_name ='z_battle_powerup_views'#line:2055
class ZBattleStageLevelupViews (BaseModel ):#line:2058
    created_at =DateTimeField (null =True )#line:2059
    scene_name =CharField ()#line:2060
    stage_level =IntegerField (index =True )#line:2061
    updated_at =DateTimeField (null =True )#line:2062
    class Meta :#line:2064
        table_name ='z_battle_stage_levelup_views'#line:2065
class ZBattleStageViews (BaseModel ):#line:2068
    created_at =DateTimeField (null =True )#line:2069
    enemy_name =CharField ()#line:2070
    enemy_nickname =CharField ()#line:2071
    enemy_resource_id =IntegerField ()#line:2072
    params =CharField ()#line:2073
    updated_at =DateTimeField (null =True )#line:2074
    z_battle_stage_id =IntegerField (index =True )#line:2075
    class Meta :#line:2077
        table_name ='z_battle_stage_views'#line:2078
class ZBattleStages (BaseModel ):#line:2081
    announcement_id =IntegerField (null =True )#line:2082
    banner_image =CharField (null =True )#line:2083
    danger_line_hp =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2084
    end_at =DateTimeField ()#line:2085
    eventkagi_end_at =DateTimeField (null =True )#line:2086
    eventkagi_start_at =DateTimeField (null =True )#line:2087
    listbutton_image =CharField (null =True )#line:2088
    locked_by =CharField (null =True )#line:2089
    priority =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2090
    start_at =DateTimeField ()#line:2091
    z_battle_stage_effect_escalation_type =IntegerField (constraints =[SQL ("DEFAULT '0'")])#line:2092
    class Meta :#line:2094
        table_name ='z_battle_stages'#line:2095
        indexes =((('eventkagi_start_at','eventkagi_end_at'),False ),)#line:2096
