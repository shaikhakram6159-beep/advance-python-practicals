st={"yr":14,"bsc2":13,"bsc3":10}
pass_dict={k:v for k,v in st.items() if v>=12}
fail_dict={k:v for k,v in st.items() if v<=12}
print("pass:",pass_dict)
print("pass:",fail_dict)