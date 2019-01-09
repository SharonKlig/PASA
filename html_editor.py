import os


def add_closing_html_tags(html_path, CONSTS, run_number):
    with open(html_path, 'a') as f:
        f.write(
            f'<hr>\n<h4 class=footer><p align=\'center\'>Questions and comments are welcome! Please ' \
            f'<span class="admin_link">' \
            f'<a href="mailto:{CONSTS.ADMIN_EMAIL}?subject={CONSTS.WEBSERVER_NAME}%20Run%20Number%20{run_number}">contact us</a>' \
            f'</span></p></h4>\n' \
            f'<div id="bottom_links" align="center"><span class="bottom_link">' \
            f'<a href="{CONSTS.WEBSERVER_URL}/" target="_blank">Home</a>' \
            f'&nbsp;|&nbsp<a href="{CONSTS.WEBSERVER_URL}/overview.html" target="_blank">Overview</a>\n' \
            f'</span>\n' \
            f'<br><br><br>\n</body>\n</html>\n')
        f.flush()

    # Must be after flushing all previous data. Otherwise it might refresh during the writing.. :(
    from time import sleep
    sleep(2 * CONSTS.RELOAD_INTERVAL)
    with open(html_path) as f:
        html_content = f.read()
    html_content = html_content.replace(CONSTS.RELOAD_TAGS, '')
    with open(html_path, 'w') as f:
        f.write(html_content)



def get_html_string_of_restult(file_name, str_to_show_on_html, final_output_dir_name='output_files'):
    result = '<tr><td>'
    result += f'<a href="{os.path.join(final_output_dir_name, file_name)}" target="_blank">{str_to_show_on_html}</a>'
    result += f'<br></td></tr>'

    return result



def edit_success_html(html_path, final_output_dir_name, run_number, CONSTS, file_names=None, strs_to_show_on_html=None):

    if file_names == None:
        file_names = ['filtered_peptides.txt', 'informative_CDR3_peptides.tsv',
                      'informative_peptides.tsv', 'non_informative_peptides.tsv',
                      'cdr3_length_distributions.png', 'IGH_D_counts.png',
                      'IGH_V_counts.png', 'IGH_J_counts.png',
                      'IGH_VD_counts.png', 'IGH_VJ_counts.png',
                      'IGH_DJ_counts.png', 'IGH_VDJ_counts.png',
                      'proteomics_vs_genetics.png']

    if strs_to_show_on_html == None:
        strs_to_show_on_html = ['List of curated peptides', 'List of informative CDR3 peptides',
                                'List of informative NON-CDR3 peptides', 'List of NON informative peptides',
                                'CDR3 length distribution', 'V family subgroup distribution',
                                'D family subgroup distribution', 'J family subgroup distribution',
                                'VD family subgroup distribution', 'VJ family subgroup distribution',
                                'DJ family subgroup distribution', 'VDJ family subgroup distribution',
                                'Proteomics VS Genetics']

    html_text = ''
    try:
        with open(html_path) as f:
            html_text = f.read()
        # The initial file exists (generate by the cgi) so we can read and parse it.
        html_text = html_text.replace('RUNNING', 'FINISHED').replace(f'{CONSTS.WEBSERVER_NAME} is now processing your request. This page will be automatically updated every {CONSTS.RELOAD_INTERVAL} seconds (until the job is done). You can also reload it manually. Once the job has finished, the output will appear below. ', '')
    except FileNotFoundError:
        import logging
        logger = logging.getLogger('main')
        logger.warning(f"Couldn't find html prefix at: {html_path}")

    html_text += f'<div class="container" style="{CONSTS.CONTAINER_STYLE}">\n' \
        f'<h2>RESULTS:<h2>'\
        f'<h3><b><a href=\'{final_output_dir_name}.zip\' target=\'_blank\'>Download zipped full results (textual & visual)</a></b></h3>' \
        f'<table class="table">\n' \
        f'<thead>\n' \
        f'<tr><th><h3>Quick access to selected results:</h3></th></tr>\n' \
        f'</thead>\n' \
        f'<tbody>'

    for i in range(len(file_names)):
        html_text += get_html_string_of_restult(file_names[i], strs_to_show_on_html[i])

    with open(html_path, 'w') as f:
        f.write(html_text)
        f.flush()

    add_closing_html_tags(html_path, CONSTS, run_number)



def edit_failure_html(html_path, run_number, msg, CONSTS):
    html_text = ''
    try:
        with open(html_path) as f:
            html_text = f.read()
        # The initial file exists (generate by the cgi) so we can read and parse it.
        html_text = html_text.replace('RUNNING', 'FAILED').replace(f'{CONSTS.WEBSERVER_NAME} is now processing your request. This page will be automatically updated every {CONSTS.RELOAD_INTERVAL} seconds (until the job is done). You can also reload it manually. Once the job has finished, several links to the output files will appear below. ', '')
    except FileNotFoundError:
        import logging
        logger = logging.getLogger('main')
        logger.warning(f"Couldn't find html prefix at: {html_path}")

    html_text +=f'<br><br><br>\n' \
                f'<center><h2>\n' \
                f'<font color="red">{msg}</font><br><br>' \
                f'Please try to re-run your job or <a href="mailto:{CONSTS.ADMIN_EMAIL}?subject={CONSTS.WEBSERVER_NAME}%20Run%20Number:%20{run_number}">contact us</a> for further information' \
                f'</h2></center>\n' \
                f'<br><br>\n' \
                f'</body>\n</html>\n'

    with open(html_path, 'w') as f:
        f.write(html_text)
        f.flush()

    add_closing_html_tags(html_path, CONSTS, run_number)

