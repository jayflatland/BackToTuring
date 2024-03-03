import os
import tempfile
import shutil

def run_asm_program_text(progtext):
    tmpdir = tempfile.mkdtemp()
    base_filename = os.path.join(tmpdir, "tmp")
    asm_file = open(base_filename + '.asm', 'w')
    asm_file.write(progtext)
    asm_file.close()

    os.system(f"nasm -f elf64 -o {base_filename}.o {base_filename}.asm")
    #TODO - check for errors here
    os.system(f"ld -m elf_x86_64 -o {base_filename}.x {base_filename}.o")
    #TODO - check for errors here
    os.system(f"{base_filename}.x")
    shutil.rmtree(tmpdir)
