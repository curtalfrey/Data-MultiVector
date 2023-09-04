# ... (other imports and code remain the same) ...

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_paths = request.form.getlist('input_paths[]')
        output_paths = request.form.getlist('output_paths[]')
        connections = request.form.getlist('connections[]')

        # Process the input_paths, output_paths, and connections as needed
        # For demonstration purposes, let's just print them
        print("Input Paths:", input_paths)
        print("Output Paths:", output_paths)
        print("Selected Connections:", connections)

    return render_template('index.html', instructions=INSTRUCTIONS)

# ... (other routes and functions remain the same) ...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

