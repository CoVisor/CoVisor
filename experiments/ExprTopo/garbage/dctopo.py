




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>ripl/ripl/dctopo.py at master · xinjin/ripl · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="xinjin/ripl" name="twitter:title" /><meta content="ripl - Python library to simplify the creation of data center code" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/2257741?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/2257741?s=400" property="og:image" /><meta content="xinjin/ripl" property="og:title" /><meta content="https://github.com/xinjin/ripl" property="og:url" /><meta content="ripl - Python library to simplify the creation of data center code" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="80708BC3:5BD8:ED7BCC4:53C43CA8" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="y6V1BVOje6MKMkS+64RfQ5gdcx+QR5RJEIHx+Mg9w3MGbuHh60Zt8KCiLo/o9m0AiOwuqb2cWqX5NtGO7pfoQw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-705bf82907ce7d9c0f30795b81517bff3b0218a0.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-7b12c21d4e47b20b15995e9a0f5f66d737e23334.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="1cbef73b93c13e05f413f0fbfbefddbc">

      
  <meta name="description" content="ripl - Python library to simplify the creation of data center code" />


  <meta content="2257741" name="octolytics-dimension-user_id" /><meta content="xinjin" name="octolytics-dimension-user_login" /><meta content="21833869" name="octolytics-dimension-repository_id" /><meta content="xinjin/ripl" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="4362711" name="octolytics-dimension-repository_parent_id" /><meta content="brandonheller/ripl" name="octolytics-dimension-repository_parent_nwo" /><meta content="4362711" name="octolytics-dimension-repository_network_root_id" /><meta content="brandonheller/ripl" name="octolytics-dimension-repository_network_root_nwo" />

  <link href="https://github.com/xinjin/ripl/commits/master.atom" rel="alternate" title="Recent Commits to ripl:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public fork page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fxinjin%2Fripl%2Fblob%2Fmaster%2Fripl%2Fdctopo.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
          <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
    data-repo="xinjin/ripl"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="xinjin/ripl" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">


  <li>
      <a href="/login?return_to=%2Fxinjin%2Fripl"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/xinjin/ripl/stargazers">
      0
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fxinjin%2Fripl"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/xinjin/ripl/network" class="social-count">
        10
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author"><a href="/xinjin" class="url fn" itemprop="url" rel="author"><span itemprop="title">xinjin</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/xinjin/ripl" class="js-current-repository js-repo-home-link">ripl</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/brandonheller/ripl">brandonheller/ripl</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/xinjin/ripl" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /xinjin/ripl">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/xinjin/ripl/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /xinjin/ripl/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/xinjin/ripl/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /xinjin/ripl/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/xinjin/ripl/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /xinjin/ripl/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/xinjin/ripl/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /xinjin/ripl/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/xinjin/ripl.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/xinjin/ripl.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/xinjin/ripl" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/xinjin/ripl" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/xinjin/ripl/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download xinjin/ripl as a zip file"
                   title="Download xinjin/ripl as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/xinjin/ripl/blob/350ff5cebef4725f4add46ab489442fe0c40d206/ripl/dctopo.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:6331ccf25b1e0a66d5dd8890eb91fff8 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/xinjin/ripl/blob/archived/class/cs244/ripl/dctopo.py"
                 data-name="archived/class/cs244"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="archived/class/cs244">archived/class/cs244</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/xinjin/ripl/blob/master/ripl/dctopo.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/xinjin/ripl/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="ripl/dctopo.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/xinjin/ripl" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ripl</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/xinjin/ripl/tree/master/ripl" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ripl</span></a></span><span class="separator"> / </span><strong class="final-path">dctopo.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="" class="main-avatar" height="24" src="https://1.gravatar.com/avatar/84ea60ea59605cfe1e5d180c8bb40d3a?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=x&amp;s=140" width="24" />
      <span class="author"><span>Brandon Heller</span></span>
      <time datetime="2013-06-21T10:27:17-07:00" is="relative-time">June 21, 2013</time>
      <div class="commit-title">
          <a href="/xinjin/ripl/commit/350ff5cebef4725f4add46ab489442fe0c40d206" class="message" data-pjax="true" title="Fix wrong comment">Fix wrong comment</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>0</strong>  contributors</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>419 lines (339 sloc)</span>
          <span class="meta-divider"></span>
        <span>13.666 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/xinjin/ripl/raw/master/ripl/dctopo.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/xinjin/ripl/blame/master/ripl/dctopo.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/xinjin/ripl/commits/master/ripl/dctopo.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="sd">&#39;&#39;&#39;@package dctopo</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="sd">Data center network topology creation and drawing.</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">@author Brandon Heller (brandonh@stanford.edu)</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">This package includes code to create and draw networks with a regular,</span></div><div class='line' id='LC9'><span class="sd">repeated structure.  The main class is StructuredTopo, which augments the</span></div><div class='line' id='LC10'><span class="sd">standard Mininet Topo object with layer metadata plus convenience functions to</span></div><div class='line' id='LC11'><span class="sd">enumerate up, down, and layer edges.</span></div><div class='line' id='LC12'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="kn">from</span> <span class="nn">mininet.topo</span> <span class="kn">import</span> <span class="n">Topo</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="n">PORT_BASE</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c"># starting index for OpenFlow switch ports</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="k">class</span> <span class="nc">NodeID</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Topo node identifier.&#39;&#39;&#39;</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dpid</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Init.</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="sd">        @param dpid dpid</span></div><div class='line' id='LC27'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># DPID-compatible hashable identifier: opaque 64-bit unsigned int</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">=</span> <span class="n">dpid</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;String conversion.</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><span class="sd">        @return str dpid as string</span></div><div class='line' id='LC35'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dpid</span><span class="p">)</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">name_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Name conversion.</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="sd">        @return name name as string</span></div><div class='line' id='LC42'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dpid</span><span class="p">)</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">ip_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Name conversion.</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><span class="sd">        @return ip ip as string</span></div><div class='line' id='LC49'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hi</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff0000</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">16</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mid</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff00</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">8</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;10.</span><span class="si">%i</span><span class="s">.</span><span class="si">%i</span><span class="s">.</span><span class="si">%i</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">hi</span><span class="p">,</span> <span class="n">mid</span><span class="p">,</span> <span class="n">lo</span><span class="p">)</span></div><div class='line' id='LC54'><br/></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="k">class</span> <span class="nc">StructuredNodeSpec</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Layer-specific vertex metadata for a StructuredTopo graph.&#39;&#39;&#39;</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">up_total</span><span class="p">,</span> <span class="n">down_total</span><span class="p">,</span> <span class="n">up_speed</span><span class="p">,</span> <span class="n">down_speed</span><span class="p">,</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">type_str</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Init.</span></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'><span class="sd">        @param up_total number of up links</span></div><div class='line' id='LC64'><span class="sd">        @param down_total number of down links</span></div><div class='line' id='LC65'><span class="sd">        @param up_speed speed in Gbps of up links</span></div><div class='line' id='LC66'><span class="sd">        @param down_speed speed in Gbps of down links</span></div><div class='line' id='LC67'><span class="sd">        @param type_str string; model of switch or server</span></div><div class='line' id='LC68'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">up_total</span> <span class="o">=</span> <span class="n">up_total</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">down_total</span> <span class="o">=</span> <span class="n">down_total</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">up_speed</span> <span class="o">=</span> <span class="n">up_speed</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">down_speed</span> <span class="o">=</span> <span class="n">down_speed</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">type_str</span> <span class="o">=</span> <span class="n">type_str</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'><span class="k">class</span> <span class="nc">StructuredEdgeSpec</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Static edge metadata for a StructuredTopo graph.&#39;&#39;&#39;</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">speed</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">):</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Init.</span></div><div class='line' id='LC81'><br/></div><div class='line' id='LC82'><span class="sd">        @param speed bandwidth in Gbps</span></div><div class='line' id='LC83'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">speed</span> <span class="o">=</span> <span class="n">speed</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'><br/></div><div class='line' id='LC87'><span class="k">class</span> <span class="nc">StructuredTopo</span><span class="p">(</span><span class="n">Topo</span><span class="p">):</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Data center network representation for structured multi-trees.&#39;&#39;&#39;</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node_specs</span><span class="p">,</span> <span class="n">edge_specs</span><span class="p">):</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Create StructuredTopo object.</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'><span class="sd">        @param node_specs list of StructuredNodeSpec objects, one per layer</span></div><div class='line' id='LC94'><span class="sd">        @param edge_specs list of StructuredEdgeSpec objects for down-links,</span></div><div class='line' id='LC95'><span class="sd">            one per layer</span></div><div class='line' id='LC96'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">StructuredTopo</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">()</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">node_specs</span> <span class="o">=</span> <span class="n">node_specs</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">edge_specs</span> <span class="o">=</span> <span class="n">edge_specs</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">layer</span><span class="p">):</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return default dict for a structured topo.</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><span class="sd">        @param layer layer of node</span></div><div class='line' id='LC105'><span class="sd">        @return d dict with layer key/val pair, plus anything else (later)</span></div><div class='line' id='LC106'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">{</span><span class="s">&#39;layer&#39;</span><span class="p">:</span> <span class="n">layer</span><span class="p">}</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">layer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return layer of a node</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'><span class="sd">        @param name name of switch</span></div><div class='line' id='LC113'><span class="sd">        @return layer layer of switch</span></div><div class='line' id='LC114'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_info</span><span class="p">[</span><span class="n">name</span><span class="p">][</span><span class="s">&#39;layer&#39;</span><span class="p">]</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isPortUp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port</span><span class="p">):</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; Returns whether port is facing up or down</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><span class="sd">        @param port port number</span></div><div class='line' id='LC121'><span class="sd">        @return portUp boolean is port facing up?</span></div><div class='line' id='LC122'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">port</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">PORT_BASE</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">layer_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">layer</span><span class="p">):</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return nodes at a provided layer.</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'><span class="sd">        @param layer layer</span></div><div class='line' id='LC129'><span class="sd">        @return names list of names</span></div><div class='line' id='LC130'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">is_layer</span><span class="p">(</span><span class="n">n</span><span class="p">):</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Returns true if node is at layer.&#39;&#39;&#39;</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">n</span><span class="p">)</span> <span class="o">==</span> <span class="n">layer</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">g</span><span class="o">.</span><span class="n">nodes</span><span class="p">()</span> <span class="k">if</span> <span class="n">is_layer</span><span class="p">(</span><span class="n">n</span><span class="p">)]</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">nodes</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">up_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return edges one layer higher (closer to core).</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'><span class="sd">        @param name name</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'><span class="sd">        @return names list of names</span></div><div class='line' id='LC144'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">layer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">name</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">g</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">n</span><span class="p">)</span> <span class="o">==</span> <span class="n">layer</span><span class="p">]</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">nodes</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">down_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return edges one layer higher (closer to hosts).</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><span class="sd">        @param name name</span></div><div class='line' id='LC153'><span class="sd">        @return names list of names</span></div><div class='line' id='LC154'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">layer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">name</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">g</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">n</span><span class="p">)</span> <span class="o">==</span> <span class="n">layer</span><span class="p">]</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">nodes</span></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">up_edges</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return edges one layer higher (closer to core).</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><span class="sd">        @param name name</span></div><div class='line' id='LC163'><span class="sd">        @return up_edges list of name pairs</span></div><div class='line' id='LC164'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edges</span> <span class="o">=</span> <span class="p">[(</span><span class="n">name</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">up_nodes</span><span class="p">(</span><span class="n">name</span><span class="p">)]</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">edges</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">down_edges</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return edges one layer lower (closer to hosts).</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="sd">        @param name name</span></div><div class='line' id='LC172'><span class="sd">        @return down_edges list of name pairs</span></div><div class='line' id='LC173'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edges</span> <span class="o">=</span> <span class="p">[(</span><span class="n">name</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">down_nodes</span><span class="p">(</span><span class="n">name</span><span class="p">)]</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">edges</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'><span class="c">#    def draw(self, filename = None, edge_width = 1, node_size = 1,</span></div><div class='line' id='LC178'><span class="c">#             node_color = &#39;g&#39;, edge_color = &#39;b&#39;):</span></div><div class='line' id='LC179'><span class="c">#        &#39;&#39;&#39;Generate image of RipL network.</span></div><div class='line' id='LC180'><span class="c">#</span></div><div class='line' id='LC181'><span class="c">#        @param filename filename w/ext to write; if None, show topo on screen</span></div><div class='line' id='LC182'><span class="c">#        @param edge_width edge width in pixels</span></div><div class='line' id='LC183'><span class="c">#        @param node_size node size in pixels</span></div><div class='line' id='LC184'><span class="c">#        @param node_color node color (ex &#39;b&#39; , &#39;green&#39;, or &#39;#0000ff&#39;)</span></div><div class='line' id='LC185'><span class="c">#        @param edge_color edge color</span></div><div class='line' id='LC186'><span class="c">#        &#39;&#39;&#39;</span></div><div class='line' id='LC187'><span class="c">#        import matplotlib.pyplot as plt</span></div><div class='line' id='LC188'><span class="c">#</span></div><div class='line' id='LC189'><span class="c">#        pos = {} # pos[vertex] = (x, y), where x, y in [0, 1]</span></div><div class='line' id='LC190'><span class="c">#        for layer in range(len(self.node_specs)):</span></div><div class='line' id='LC191'><span class="c">#            v_boxes = len(self.node_specs)</span></div><div class='line' id='LC192'><span class="c">#            height = 1 - ((layer + 0.5) / v_boxes)</span></div><div class='line' id='LC193'><span class="c">#</span></div><div class='line' id='LC194'><span class="c">#            layer_nodes = sorted(self.layer_nodes(layer, False))</span></div><div class='line' id='LC195'><span class="c">#            h_boxes = len(layer_nodes)</span></div><div class='line' id='LC196'><span class="c">#            for j, dpid in enumerate(layer_nodes):</span></div><div class='line' id='LC197'><span class="c">#                pos[dpid] = ((j + 0.5) / h_boxes, height)</span></div><div class='line' id='LC198'><span class="c">#</span></div><div class='line' id='LC199'><span class="c">#        fig = plt.figure(1)</span></div><div class='line' id='LC200'><span class="c">#        fig.clf()</span></div><div class='line' id='LC201'><span class="c">#        ax = fig.add_axes([0, 0, 1, 1], frameon = False)</span></div><div class='line' id='LC202'><span class="c">#</span></div><div class='line' id='LC203'><span class="c">#        draw_networkx_nodes(self.g, pos, ax = ax, node_size = node_size,</span></div><div class='line' id='LC204'><span class="c">#                               node_color = node_color, with_labels = False)</span></div><div class='line' id='LC205'><span class="c">#        # Work around networkx bug; does not handle color arrays properly</span></div><div class='line' id='LC206'><span class="c">#        for edge in self.edges(False):</span></div><div class='line' id='LC207'><span class="c">#            draw_networkx_edges(self.g, pos, [edge], ax = ax,</span></div><div class='line' id='LC208'><span class="c">#                                edge_color = edge_color, width = edge_width)</span></div><div class='line' id='LC209'><span class="c">#</span></div><div class='line' id='LC210'><span class="c">#        # Work around networkx modifying axis limits</span></div><div class='line' id='LC211'><span class="c">#        ax.set_xlim(0, 1.0)</span></div><div class='line' id='LC212'><span class="c">#        ax.set_ylim(0, 1.0)</span></div><div class='line' id='LC213'><span class="c">#        ax.set_axis_off()</span></div><div class='line' id='LC214'><span class="c">#</span></div><div class='line' id='LC215'><span class="c">#        if filename:</span></div><div class='line' id='LC216'><span class="c">#            plt.savefig(filename)</span></div><div class='line' id='LC217'><span class="c">#        else:</span></div><div class='line' id='LC218'><span class="c">#            plt.show()</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'><span class="k">class</span> <span class="nc">FatTreeTopo</span><span class="p">(</span><span class="n">StructuredTopo</span><span class="p">):</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Three-layer homogeneous Fat Tree.</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><span class="sd">    From &quot;A scalable, commodity data center network architecture, M. Fares et</span></div><div class='line' id='LC225'><span class="sd">    al. SIGCOMM 2008.&quot;</span></div><div class='line' id='LC226'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_CORE</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_AGG</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_EDGE</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_HOST</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC231'><br/></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">class</span> <span class="nc">FatTreeNodeID</span><span class="p">(</span><span class="n">NodeID</span><span class="p">):</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Fat Tree-specific node.&#39;&#39;&#39;</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pod</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">sw</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">host</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">dpid</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">name</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Create FatTreeNodeID object from custom params.</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="sd">            Either (pod, sw, host) or dpid must be passed in.</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><span class="sd">            @param pod pod ID</span></div><div class='line' id='LC241'><span class="sd">            @param sw switch ID</span></div><div class='line' id='LC242'><span class="sd">            @param host host ID</span></div><div class='line' id='LC243'><span class="sd">            @param dpid optional dpid</span></div><div class='line' id='LC244'><span class="sd">            @param name optional name</span></div><div class='line' id='LC245'><span class="sd">            &#39;&#39;&#39;</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dpid</span><span class="p">:</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pod</span> <span class="o">=</span> <span class="p">(</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff0000</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">16</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sw</span> <span class="o">=</span> <span class="p">(</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff00</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">8</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="p">(</span><span class="n">dpid</span> <span class="o">&amp;</span> <span class="mh">0xff</span><span class="p">)</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">=</span> <span class="n">dpid</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">name</span><span class="p">:</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pod</span><span class="p">,</span> <span class="n">sw</span><span class="p">,</span> <span class="n">host</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;_&#39;</span><span class="p">)]</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pod</span> <span class="o">=</span> <span class="n">pod</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sw</span> <span class="o">=</span> <span class="n">sw</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">host</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">=</span> <span class="p">(</span><span class="n">pod</span> <span class="o">&lt;&lt;</span> <span class="mi">16</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">sw</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">host</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pod</span> <span class="o">=</span> <span class="n">pod</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sw</span> <span class="o">=</span> <span class="n">sw</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">host</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dpid</span> <span class="o">=</span> <span class="p">(</span><span class="n">pod</span> <span class="o">&lt;&lt;</span> <span class="mi">16</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">sw</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">+</span> <span class="n">host</span></div><div class='line' id='LC262'><br/></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;(</span><span class="si">%i</span><span class="s">, </span><span class="si">%i</span><span class="s">, </span><span class="si">%i</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pod</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sw</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">)</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">name_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return name string&#39;&#39;&#39;</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;</span><span class="si">%i</span><span class="s">_</span><span class="si">%i</span><span class="s">_</span><span class="si">%i</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pod</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sw</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">)</span></div><div class='line' id='LC269'><br/></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">mac_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return MAC string&#39;&#39;&#39;</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;00:00:00:</span><span class="si">%02x</span><span class="s">:</span><span class="si">%02x</span><span class="s">:</span><span class="si">%02x</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pod</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sw</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">)</span></div><div class='line' id='LC273'><br/></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">ip_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return IP string&#39;&#39;&#39;</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;10.</span><span class="si">%i</span><span class="s">.</span><span class="si">%i</span><span class="s">.</span><span class="si">%i</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pod</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sw</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">host</span><span class="p">)</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC278'><span class="sd">    def _add_port(self, src, dst):</span></div><div class='line' id='LC279'><span class="sd">        &#39;&#39;&#39;Generate port mapping for new edge.</span></div><div class='line' id='LC280'><br/></div><div class='line' id='LC281'><span class="sd">        Since Node IDs are assumed hierarchical and unique, we don&#39;t need to</span></div><div class='line' id='LC282'><span class="sd">        maintain a port mapping.  Instead, compute port values directly from</span></div><div class='line' id='LC283'><span class="sd">        node IDs and topology knowledge, statelessly, for calls to self.port.</span></div><div class='line' id='LC284'><br/></div><div class='line' id='LC285'><span class="sd">        @param src source switch DPID</span></div><div class='line' id='LC286'><span class="sd">        @param dst destination switch DPID</span></div><div class='line' id='LC287'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC288'><span class="sd">        pass</span></div><div class='line' id='LC289'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">layer</span><span class="p">,</span> <span class="n">name</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return default dict for a FatTree topo.</span></div><div class='line' id='LC292'><br/></div><div class='line' id='LC293'><span class="sd">        @param layer layer of node</span></div><div class='line' id='LC294'><span class="sd">        @param name name of node</span></div><div class='line' id='LC295'><span class="sd">        @return d dict with layer key/val pair, plus anything else (later)</span></div><div class='line' id='LC296'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;layer&#39;</span><span class="p">:</span> <span class="n">layer</span><span class="p">}</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">name</span><span class="p">:</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="p">)</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># For hosts only, set the IP</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">layer</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">LAYER_HOST</span><span class="p">:</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="s">&#39;ip&#39;</span><span class="p">:</span> <span class="nb">id</span><span class="o">.</span><span class="n">ip_str</span><span class="p">()})</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="s">&#39;mac&#39;</span><span class="p">:</span> <span class="nb">id</span><span class="o">.</span><span class="n">mac_str</span><span class="p">()})</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="s">&#39;dpid&#39;</span><span class="p">:</span> <span class="s">&quot;</span><span class="si">%016x</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">id</span><span class="o">.</span><span class="n">dpid</span><span class="p">})</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">d</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'><br/></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span> <span class="n">speed</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">):</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Init.</span></div><div class='line' id='LC310'><br/></div><div class='line' id='LC311'><span class="sd">        @param k switch degree</span></div><div class='line' id='LC312'><span class="sd">        @param speed bandwidth in Gbps</span></div><div class='line' id='LC313'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">core</span> <span class="o">=</span> <span class="n">StructuredNodeSpec</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">k</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span> <span class="n">type_str</span> <span class="o">=</span> <span class="s">&#39;core&#39;</span><span class="p">)</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">agg</span> <span class="o">=</span> <span class="n">StructuredNodeSpec</span><span class="p">(</span><span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span> <span class="n">type_str</span> <span class="o">=</span> <span class="s">&#39;agg&#39;</span><span class="p">)</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edge</span> <span class="o">=</span> <span class="n">StructuredNodeSpec</span><span class="p">(</span><span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">type_str</span> <span class="o">=</span> <span class="s">&#39;edge&#39;</span><span class="p">)</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">host</span> <span class="o">=</span> <span class="n">StructuredNodeSpec</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">speed</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">type_str</span> <span class="o">=</span> <span class="s">&#39;host&#39;</span><span class="p">)</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">node_specs</span> <span class="o">=</span> <span class="p">[</span><span class="n">core</span><span class="p">,</span> <span class="n">agg</span><span class="p">,</span> <span class="n">edge</span><span class="p">,</span> <span class="n">host</span><span class="p">]</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edge_specs</span> <span class="o">=</span> <span class="p">[</span><span class="n">StructuredEdgeSpec</span><span class="p">(</span><span class="n">speed</span><span class="p">)]</span> <span class="o">*</span> <span class="mi">3</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">FatTreeTopo</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">node_specs</span><span class="p">,</span> <span class="n">edge_specs</span><span class="p">)</span></div><div class='line' id='LC322'><br/></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">k</span> <span class="o">=</span> <span class="n">k</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span> <span class="o">=</span> <span class="n">FatTreeTopo</span><span class="o">.</span><span class="n">FatTreeNodeID</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">numPods</span> <span class="o">=</span> <span class="n">k</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">aggPerPod</span> <span class="o">=</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC327'><br/></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pods</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">core_sws</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">agg_sws</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edge_sws</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hosts</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC333'><br/></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">pods</span><span class="p">:</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">edge_sws</span><span class="p">:</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edge_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">name_str</span><span class="p">()</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">edge_opts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LAYER_EDGE</span><span class="p">,</span> <span class="n">edge_id</span><span class="p">)</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addSwitch</span><span class="p">(</span><span class="n">edge_id</span><span class="p">,</span> <span class="o">**</span><span class="n">edge_opts</span><span class="p">)</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">h</span> <span class="ow">in</span> <span class="n">hosts</span><span class="p">:</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">host_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">h</span><span class="p">)</span><span class="o">.</span><span class="n">name_str</span><span class="p">()</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">host_opts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LAYER_HOST</span><span class="p">,</span> <span class="n">host_id</span><span class="p">)</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addHost</span><span class="p">(</span><span class="n">host_id</span><span class="p">,</span> <span class="o">**</span><span class="n">host_opts</span><span class="p">)</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addLink</span><span class="p">(</span><span class="n">host_id</span><span class="p">,</span> <span class="n">edge_id</span><span class="p">)</span></div><div class='line' id='LC345'><br/></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">agg_sws</span><span class="p">:</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">agg_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">name_str</span><span class="p">()</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">agg_opts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LAYER_AGG</span><span class="p">,</span> <span class="n">agg_id</span><span class="p">)</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addSwitch</span><span class="p">(</span><span class="n">agg_id</span><span class="p">,</span> <span class="o">**</span><span class="n">agg_opts</span><span class="p">)</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addLink</span><span class="p">(</span><span class="n">edge_id</span><span class="p">,</span> <span class="n">agg_id</span><span class="p">)</span></div><div class='line' id='LC351'><br/></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">agg_sws</span><span class="p">:</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">agg_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">name_str</span><span class="p">()</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">c_index</span> <span class="o">=</span> <span class="n">a</span> <span class="o">-</span> <span class="n">k</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">core_sws</span><span class="p">:</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">core_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">c_index</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span><span class="o">.</span><span class="n">name_str</span><span class="p">()</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">core_opts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">def_nopts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">LAYER_CORE</span><span class="p">,</span> <span class="n">core_id</span><span class="p">)</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addSwitch</span><span class="p">(</span><span class="n">core_id</span><span class="p">,</span> <span class="o">**</span><span class="n">core_opts</span><span class="p">)</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">addLink</span><span class="p">(</span><span class="n">core_id</span><span class="p">,</span> <span class="n">agg_id</span><span class="p">)</span></div><div class='line' id='LC360'><br/></div><div class='line' id='LC361'><br/></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">src</span><span class="p">,</span> <span class="n">dst</span><span class="p">):</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Get port number (optional)</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'><span class="sd">        Note that the topological significance of DPIDs in FatTreeTopo enables</span></div><div class='line' id='LC366'><span class="sd">        this function to be implemented statelessly.</span></div><div class='line' id='LC367'><br/></div><div class='line' id='LC368'><span class="sd">        @param src source switch name</span></div><div class='line' id='LC369'><span class="sd">        @param dst destination switch name</span></div><div class='line' id='LC370'><span class="sd">        @return tuple (src_port, dst_port):</span></div><div class='line' id='LC371'><span class="sd">            src_port: port on source switch leading to the destination switch</span></div><div class='line' id='LC372'><span class="sd">            dst_port: port on destination switch leading to the source switch</span></div><div class='line' id='LC373'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_layer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">src</span><span class="p">)</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_layer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layer</span><span class="p">(</span><span class="n">dst</span><span class="p">)</span></div><div class='line' id='LC376'><br/></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">name</span> <span class="o">=</span> <span class="n">src</span><span class="p">)</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id_gen</span><span class="p">(</span><span class="n">name</span> <span class="o">=</span> <span class="n">dst</span><span class="p">)</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_CORE</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_AGG</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_EDGE</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LAYER_HOST</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC384'><br/></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_HOST</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span><span class="p">:</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">src_id</span><span class="o">.</span><span class="n">host</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_CORE</span><span class="p">:</span></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">dst_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="n">src_id</span><span class="o">.</span><span class="n">pod</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_AGG</span><span class="p">:</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">dst_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="n">src_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_AGG</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_CORE</span><span class="p">:</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">dst_id</span><span class="o">.</span><span class="n">host</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="n">src_id</span><span class="o">.</span><span class="n">pod</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_CORE</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_AGG</span><span class="p">:</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="n">dst_id</span><span class="o">.</span><span class="n">pod</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">src_id</span><span class="o">.</span><span class="n">host</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_AGG</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span><span class="p">:</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="n">dst_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">src_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">k</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_CORE</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span><span class="p">:</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="n">dst_id</span><span class="o">.</span><span class="n">pod</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">src_id</span><span class="o">.</span><span class="n">sw</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">src_layer</span> <span class="o">==</span> <span class="n">LAYER_EDGE</span> <span class="ow">and</span> <span class="n">dst_layer</span> <span class="o">==</span> <span class="n">LAYER_HOST</span><span class="p">:</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">=</span> <span class="p">(</span><span class="n">dst_id</span><span class="o">.</span><span class="n">host</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;Could not find port leading to given dst switch&quot;</span><span class="p">)</span></div><div class='line' id='LC411'><br/></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Shift by one; as of v0.9, OpenFlow ports are 1-indexed.</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">src_layer</span> <span class="o">!=</span> <span class="n">LAYER_HOST</span><span class="p">:</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">src_port</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dst_layer</span> <span class="o">!=</span> <span class="n">LAYER_HOST</span><span class="p">:</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dst_port</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC417'><br/></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="n">src_port</span><span class="p">,</span> <span class="n">dst_port</span><span class="p">)</span></div><div class='line' id='LC419'>&nbsp;&nbsp;</div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.03280s from github-fe131-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-df9e4beac80276ed3dfa56be0d97b536d0f5ee12.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-e4591d88d498b849f06ae49e0a07d6c6401ac7c7.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

