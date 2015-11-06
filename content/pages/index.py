# -*- coding: utf-8 -*-
import os
from pydozer import Page

index_page = Page()
index_page.data['filename'] = os.path.basename(__file__).replace('.pyc', '').replace('.py', '')

index_page.data['title'] = "Blunt Consultants - Solving Problems Faster, Leaving The Flashy Bits At Home"
index_page.data['is_home'] = True
index_page.data['content'] = """
        <!-- One -->
            <section id="one" class="wrapper style2 special">
                <header class="major">
                    <h2>We're busy. Maybe you are too.<br />
                    If you needs us, and can pay us,<br />
                    we might help you solve some issues.<br />
                    Just don't expect fanfare.</h2>
                </header>
                <p><a href="https://phonejanitor.com"><span class="icon fa-phone">&nbsp;</span>We're focused on Phone Janitor</a></p>
                <p>But we sometimes have cycles to spare now and then. That's how our talent works.</p>
            </section>

        <!-- Two -->
            <section id="two" class="wrapper">
                <div class="inner alt">
                    <section class="spotlight">
                        <div class="content">
                            <h3>We architect and we code.</h3>
                            <p>We're not interested in doing anything else for you.  If you want to know how to do your software project right, we can tell you.  Professionally and directly as possible.  You'll feel comfortable that it's the truth because we'll have no stake in it otherwise.</p>
                        </div>
                    </section>
                    <section class="spotlight">
                        <div class="content">
                            <h3>Python, Java, Javascript, K</h3>
                            <p>These are the languages we work in.  Need something else?  We're probably not interested ourselves.  Ask for a referral if you need one.</p>
                        </div>
                    </section>
                    <section class="spotlight">
                        <div class="content">
                            <h3>Angular, React, FreeSWITCH, Pyramid, Postgres</h3>
                            <p>These are about the only buzz worthy things we are focused on right now.  If you've got something else, ask, but we may just tell you we're not the best fit.</p>
                        </div>
                    </section>
                    <section class="special">
                        <ul class="icons labeled">
                            <li><span class="icon fa-simplybuilt"><span class="label">Simple Solutions</span></span></li>
                            <li><span class="icon fa-wrench"><span class="label">Easily maintained</span></span></li>
                            <li><span class="icon fa-flash"><span class="label">No flash</span></span></li>
                            <li><span class="icon fa-trash"><span class="label">No wasting time</span></span></li>
                        </ul>
                    </section>
                </div>
            </section>

        <!-- Three -->
            <section id="three" class="wrapper style2 special">
                <header class="major">
                    <h2>We're not cheap</h2>
                    <p>We're good, we're fast, but we earn it.  If you're serious, let's talk.<br />
                    If you want someone to make you feel special, there's yes-men out there.  We'll make you feel like everyone wins.</p>
                </header>
                <ul class="actions">
                    <li><a href="mailto:consulting@networksanitationcommittee.com" class="button">Drop a Line</a></li>
                </ul>
            </section>

"""
