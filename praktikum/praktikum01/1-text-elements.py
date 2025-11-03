import streamlit as st

st.header("Ini Header")
st.subheader("Ini Subheader")
st.text("Ini Text Biasa")
st.markdown("Ini *Markdown* dengan **teks tebal** dan _teks miring_.")
st.markdown("""
            ini adalah paragraf pertama.
            ini adalah paragraf kedua.
            ini adalah paragraf ketiga.
            321""")
st.caption("Ini adalah caption untuk gambar atau elemen lainnya.")
st.title("Ini Title untuk halaman atau bagian tertentu.")

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 1")
st.markdown("""
            Nama Lengkap : Ahmad Al-Faqih Asasi
            NIM          : 0110222190
            """)

st.header("Dispalay LaTeX")
st.latex(r''' (a + b)^2 = a^2 + 2ab + b^2 ''')

st.header("Display Code")
st.subheader("Pthon Code")

code = '''
def hello():
    print("Hello Streamlit!")'''
st.code(code, language='python')


st.subheader("Java Code")
st.code('''
        public class GFG {
            public static void main(String[] args)
            {
                System.out.println("Hello World");
            }
}''', language='java')


st.subheader("JavaScript Code")
st.code("""
<script>
try {
        addalert("Welcome guest!"); //sengaja salah ketik (addalert bukan alert) 
}
        catch (err) {
        document.getElementById("demo").innerHTML = err.message;
        menampilkanPesan error di elemen HTML dengan id='demo'
}
</script>
""", language='javascript')

