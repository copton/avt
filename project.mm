<map version="0.7.1">
<node TEXT="voctrain+">
<node TEXT="lookup" POSITION="right">
<node TEXT="backends">
<node TEXT="dict.leo.org">
<node TEXT="get and parse http"/>
</node>
<node TEXT="trans/de-en">
<node TEXT="parser from voctrain"/>
</node>
<node TEXT="database"/>
</node>
</node>
<node TEXT="learn" POSITION="left">
<node TEXT="learn the most frequent words first">
<node TEXT="right answers are scored down&#xa;wrong answers are scored up">
<node TEXT="find proper scorings">
<node TEXT="start with +/- 1"/>
</node>
</node>
<node TEXT="no levels any more"/>
</node>
<node TEXT="learn word by meaning">
<node TEXT="provide example sentence"/>
</node>
</node>
<node TEXT="database" POSITION="right">
<node TEXT="rational database model">
<node TEXT="sqlite3"/>
<node TEXT="word">
<node TEXT="+ translation"/>
<node TEXT="+ sentence"/>
</node>
</node>
</node>
<node TEXT="ui" POSITION="left">
<node TEXT="console"/>
<node TEXT="android"/>
</node>
</node>
</map>
