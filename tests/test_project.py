"""
Test suite for Jekyll/Reveal.js presentation project.
Tests configuration, layouts, includes, posts, and scripts.
"""

import os
import unittest
import yaml
from pathlib import Path


class TestConfig(unittest.TestCase):
    """Tests for _config.yml configuration file."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
        cls.config_file = cls.root_dir / '_config.yml'
    
    def test_config_file_exists(self):
        """_config.yml should exist."""
        self.assertTrue(self.config_file.exists(), "_config.yml should exist")
    
    def test_config_has_required_fields(self):
        """Config should have required fields."""
        with open(self.config_file) as f:
            config = yaml.safe_load(f)
        
        self.assertIn('title', config, "Config should have a title")
        self.assertIn('description', config, "Config should have a description")
        self.assertIn('markdown', config, "Config should specify markdown processor")
        self.assertIn('highlighter', config, "Config should specify highlighter")
    
    def test_markdown_is_kramdown(self):
        """Markdown should be set to kramdown."""
        with open(self.config_file) as f:
            config = yaml.safe_load(f)
        
        self.assertEqual(config.get('markdown'), 'kramdown', 
                        "Markdown should be set to kramdown")
    
    def test_highlighter_is_rouge(self):
        """Highlighter should be set to rouge."""
        with open(self.config_file) as f:
            config = yaml.safe_load(f)
        
        self.assertEqual(config.get('highlighter'), 'rouge',
                        "Highlighter should be set to rouge")
    
    def test_plugins_include_jemoji(self):
        """Plugins should include jemoji."""
        with open(self.config_file) as f:
            config = yaml.safe_load(f)
        
        plugins = config.get('plugins', [])
        self.assertIn('jemoji', plugins, "Plugins should include jemoji")


class TestLayouts(unittest.TestCase):
    """Tests for layout files."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
        cls.layouts_dir = cls.root_dir / '_layouts'
    
    def test_layouts_directory_exists(self):
        """_layouts directory should exist."""
        self.assertTrue(self.layouts_dir.exists(), "_layouts directory should exist")
    
    def test_presentation_layout_exists(self):
        """presentation.html layout should exist."""
        layout_file = self.layouts_dir / 'presentation.html'
        self.assertTrue(layout_file.exists(), "presentation.html should exist")
    
    def test_slide_layout_exists(self):
        """slide.html layout should exist."""
        layout_file = self.layouts_dir / 'slide.html'
        self.assertTrue(layout_file.exists(), "slide.html should exist")
    
    def test_print_layout_exists(self):
        """print.html layout should exist."""
        layout_file = self.layouts_dir / 'print.html'
        self.assertTrue(layout_file.exists(), "print.html should exist")
    
    def test_presentation_layout_has_required_structure(self):
        """presentation.html should have required HTML structure."""
        layout_file = self.layouts_dir / 'presentation.html'
        content = layout_file.read_text()
        
        self.assertIn('<!DOCTYPE html>', content, "Should have DOCTYPE declaration")
        self.assertIn('<html', content, "Should have html tag")
        self.assertIn('<head>', content, "Should have head tag")
        self.assertIn('<body>', content, "Should have body tag")
        self.assertIn('{{ content }}', content, "Should include content placeholder")
        self.assertIn('include head.html', content, "Should include head.html")
        self.assertIn('include script.html', content, "Should include script.html")
    
    def test_slide_layout_has_required_structure(self):
        """slide.html should have required HTML structure."""
        layout_file = self.layouts_dir / 'slide.html'
        content = layout_file.read_text()
        
        self.assertIn('<!DOCTYPE html>', content, "Should have DOCTYPE declaration")
        self.assertIn('<html', content, "Should have html tag")
        self.assertIn('{{ content }}', content, "Should include content placeholder")
    
    def test_print_layout_has_required_structure(self):
        """print.html should have required HTML structure."""
        layout_file = self.layouts_dir / 'print.html'
        content = layout_file.read_text()
        
        self.assertIn('<!DOCTYPE html>', content, "Should have DOCTYPE declaration")
        self.assertIn('{{ content }}', content, "Should include content placeholder")


class TestIncludes(unittest.TestCase):
    """Tests for include files."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
        cls.includes_dir = cls.root_dir / '_includes'
    
    def test_includes_directory_exists(self):
        """_includes directory should exist."""
        self.assertTrue(self.includes_dir.exists(), "_includes directory should exist")
    
    def test_head_include_exists(self):
        """head.html include should exist."""
        include_file = self.includes_dir / 'head.html'
        self.assertTrue(include_file.exists(), "head.html should exist")
    
    def test_script_include_exists(self):
        """script.html include should exist."""
        include_file = self.includes_dir / 'script.html'
        self.assertTrue(include_file.exists(), "script.html should exist")
    
    def test_slide_include_exists(self):
        """slide.html include should exist."""
        include_file = self.includes_dir / 'slide.html'
        self.assertTrue(include_file.exists(), "slide.html should exist")
    
    def test_head_include_has_meta_charset(self):
        """head.html should have UTF-8 charset meta tag."""
        include_file = self.includes_dir / 'head.html'
        content = include_file.read_text()
        
        self.assertIn('charset="utf-8"', content.lower() or "charset='utf-8'" in content.lower(),
                     "Should have UTF-8 charset meta tag")
    
    def test_head_include_has_viewport_meta(self):
        """head.html should have viewport meta tag."""
        include_file = self.includes_dir / 'head.html'
        content = include_file.read_text()
        
        self.assertIn('viewport', content, "Should have viewport meta tag")
    
    def test_head_include_has_title(self):
        """head.html should have title tag."""
        include_file = self.includes_dir / 'head.html'
        content = include_file.read_text()
        
        self.assertIn('<title>', content, "Should have title tag")
    
    def test_head_include_links_reveal_css(self):
        """head.html should link to reveal.js CSS."""
        include_file = self.includes_dir / 'head.html'
        content = include_file.read_text()
        
        self.assertIn('reveal.css', content, "Should link to reveal.js CSS")
    
    def test_script_include_loads_reveal_js(self):
        """script.html should load reveal.js."""
        include_file = self.includes_dir / 'script.html'
        content = include_file.read_text()
        
        self.assertIn('reveal.js', content, "Should load reveal.js")
    
    def test_script_include_initializes_reveal(self):
        """script.html should initialize Reveal."""
        include_file = self.includes_dir / 'script.html'
        content = include_file.read_text()
        
        self.assertIn('Reveal.initialize', content, "Should initialize Reveal")
    
    def test_slide_include_has_section_tag(self):
        """slide.html should have section tag."""
        include_file = self.includes_dir / 'slide.html'
        content = include_file.read_text()
        
        self.assertIn('<section', content, "Should have section tag")


class TestPosts(unittest.TestCase):
    """Tests for posts directory and content."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
        cls.posts_dir = cls.root_dir / '_posts'
    
    def test_posts_directory_exists(self):
        """_posts directory should exist."""
        self.assertTrue(self.posts_dir.exists(), "_posts directory should exist")
    
    def test_has_at_least_one_post(self):
        """Should have at least one post."""
        posts = list(self.posts_dir.glob('*.md'))
        self.assertGreaterEqual(len(posts), 1, "Should have at least one post")
    
    def test_intro_post_exists(self):
        """Intro post (0000-01-01-intro.md) should exist."""
        intro_post = self.posts_dir / '0000-01-01-intro.md'
        self.assertTrue(intro_post.exists(), "Intro post should exist")
    
    def test_intro_post_has_front_matter(self):
        """Intro post should have front matter."""
        intro_post = self.posts_dir / '0000-01-01-intro.md'
        content = intro_post.read_text()
        
        self.assertIn('---', content, "Should have front matter delimiters")
        self.assertIn('layout:', content, "Should specify layout in front matter")
        self.assertIn('title:', content, "Should specify title in front matter")
    
    def test_intro_post_has_layout_slide(self):
        """Intro post should use slide layout."""
        intro_post = self.posts_dir / '0000-01-01-intro.md'
        content = intro_post.read_text()
        
        self.assertIn('layout: slide', content, "Intro post should use slide layout")
    
    def test_posts_have_valid_front_matter_format(self):
        """All posts should have valid front matter format."""
        for post_file in self.posts_dir.glob('*.md'):
            content = post_file.read_text()
            self.assertTrue(content.startswith('---'),
                          f"{post_file.name} should start with front matter delimiter")


class TestScripts(unittest.TestCase):
    """Tests for script files."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
        cls.script_dir = cls.root_dir / 'script'
    
    def test_script_directory_exists(self):
        """script directory should exist."""
        self.assertTrue(self.script_dir.exists(), "script directory should exist")
    
    def test_setup_script_exists(self):
        """setup script should exist."""
        setup_script = self.script_dir / 'setup'
        self.assertTrue(setup_script.exists(), "setup script should exist")
    
    def test_server_script_exists(self):
        """server script should exist."""
        server_script = self.script_dir / 'server'
        self.assertTrue(server_script.exists(), "server script should exist")
    
    def test_cibuild_script_exists(self):
        """cibuild script should exist."""
        cibuild_script = self.script_dir / 'cibuild'
        self.assertTrue(cibuild_script.exists(), "cibuild script should exist")
    
    def test_setup_script_is_executable(self):
        """setup script should be executable."""
        setup_script = self.script_dir / 'setup'
        self.assertTrue(os.access(setup_script, os.X_OK), "setup script should be executable")
    
    def test_server_script_is_executable(self):
        """server script should be executable."""
        server_script = self.script_dir / 'server'
        self.assertTrue(os.access(server_script, os.X_OK), "server script should be executable")
    
    def test_cibuild_script_is_executable(self):
        """cibuild script should be executable."""
        cibuild_script = self.script_dir / 'cibuild'
        self.assertTrue(os.access(cibuild_script, os.X_OK), "cibuild script should be executable")
    
    def test_server_script_runs_jekyll(self):
        """server script should run jekyll serve."""
        server_script = self.script_dir / 'server'
        content = server_script.read_text()
        
        self.assertIn('jekyll serve', content, "Server script should run jekyll serve")
    
    def test_cibuild_script_builds_site(self):
        """cibuild script should run jekyll build."""
        cibuild_script = self.script_dir / 'cibuild'
        content = cibuild_script.read_text()
        
        self.assertIn('jekyll build', content, "Cibuild script should run jekyll build")
    
    def test_cibuild_script_runs_htmlproofer(self):
        """cibuild script should run htmlproofer."""
        cibuild_script = self.script_dir / 'cibuild'
        content = cibuild_script.read_text()
        
        self.assertIn('htmlproofer', content, "Cibuild script should run htmlproofer")


class TestRootFiles(unittest.TestCase):
    """Tests for root level files."""
    
    @classmethod
    def setUpClass(cls):
        cls.root_dir = Path(__file__).parent.parent
    
    def test_config_file_exists(self):
        """_config.yml should exist."""
        config_file = self.root_dir / '_config.yml'
        self.assertTrue(config_file.exists(), "_config.yml should exist")
    
    def test_gemfile_exists(self):
        """Gemfile should exist."""
        gemfile = self.root_dir / 'Gemfile'
        self.assertTrue(gemfile.exists(), "Gemfile should exist")
    
    def test_index_html_exists(self):
        """index.html should exist."""
        index_file = self.root_dir / 'index.html'
        self.assertTrue(index_file.exists(), "index.html should exist")
    
    def test_readme_exists(self):
        """README.md should exist."""
        readme_file = self.root_dir / 'README.md'
        self.assertTrue(readme_file.exists(), "README.md should exist")
    
    def test_license_exists(self):
        """LICENSE should exist."""
        license_file = self.root_dir / 'LICENSE'
        self.assertTrue(license_file.exists(), "LICENSE should exist")
    
    def test_index_has_presentation_layout(self):
        """index.html should use presentation layout."""
        index_file = self.root_dir / 'index.html'
        content = index_file.read_text()
        
        self.assertIn('layout: presentation', content,
                     "index.html should use presentation layout")
    
    def test_index_loops_through_posts(self):
        """index.html should loop through posts."""
        index_file = self.root_dir / 'index.html'
        content = index_file.read_text()
        
        self.assertIn('for post in site.posts', content,
                     "index.html should loop through posts")
    
    def test_index_includes_slide(self):
        """index.html should include slide.html."""
        index_file = self.root_dir / 'index.html'
        content = index_file.read_text()
        
        self.assertIn('include slide.html', content,
                     "index.html should include slide.html")


if __name__ == '__main__':
    unittest.main()
