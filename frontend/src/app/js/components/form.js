import React from 'react';
import { Field, reduxForm } from 'redux-form';

const Form = props => {
  const { handleSubmit, pristine, reset, submitting } = props;
  return (
    <form onSubmit={handleSubmit} className="Form">
      <div>
        <div >
          <Field
            name="inputText"
            component="input"
            type="text"
            placeholder="Input Text"
          />

        </div>
        <button type="button">+</button>
      </div>
      <div>
        <button type="submit" disabled={pristine || submitting}>Analyze it!</button>
      </div>
    </form>
  );
};

export default reduxForm({
  form: 'inputText', // a unique identifier for this form
})(Form);
