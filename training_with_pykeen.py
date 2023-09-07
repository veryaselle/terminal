import pandas as pd
from sklearn.model_selection import train_test_split
from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

# Path to your triples file
triples_file = "/work/users/ao582fpoy/train/tsv_track_allowed.tsv"

# Read the triples file into a pandas DataFrame
df = pd.read_csv(triples_file, sep='\t', header=None, names=['subject', 'relation', 'object'])

# Splitting into training, validation, and test sets
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# Save the split DataFrames to TSV files
train_df.to_csv('/work/users/ao582fpoy/train/train_set.tsv', sep='\t', index=False)
val_df.to_csv('/work/users/ao582fpoy/train/validation_set.tsv', sep='\t', index=False)
test_df.to_csv('/work/users/ao582fpoy/train/test_set.tsv', sep='\t', index=False)

# Create TriplesFactory instances for each split
train_triples_factory = TriplesFactory.from_path('/work/users/ao582fpoy/train/train_set.tsv', delimiter="\t")
val_triples_factory = TriplesFactory.from_path('/work/users/ao582fpoy/train/validation_set.tsv', delimiter="\t")
test_triples_factory = TriplesFactory.from_path('/work/users/ao582fpoy/train/test_set.tsv', delimiter="\t")

# Print the number of triples and unique entities and relations for each split
print(f"Train triples: {len(train_triples_factory.triples)}")
print(f"Train entities: {train_triples_factory.num_entities}")
print(f"Train relations: {train_triples_factory.num_relations}")

print(f"Validation triples: {len(val_triples_factory.triples)}")
print(f"Validation entities: {val_triples_factory.num_entities}")
print(f"Validation relations: {val_triples_factory.num_relations}")

print(f"Test triples: {len(test_triples_factory.triples)}")
print(f"Test entities: {test_triples_factory.num_entities}")
print(f"Test relations: {test_triples_factory.num_relations}")

# Define the pipeline configuration with TransE model
pipeline_config = dict(
    model='TransE',
    model_kwargs=dict(
        embedding_dim=50,
        scoring_fct_norm=1,
    ),
    loss='margin_ranking',
    loss_kwargs=dict(margin=1),
    regularizer='LpRegularizer',
    regularizer_kwargs=dict(p=2, weight=1e-5),
    optimizer='Adam',
    optimizer_kwargs=dict(lr=0.001),
    training_loop='SLCWATrainingLoop',
    training_kwargs=dict(num_epochs=100, batch_size=64),
    stopper='early',
    stopper_kwargs=dict(patience=5),
    evaluator_kwargs=dict(filtered=True),
)

# Train and evaluate the model using the pipeline
results = pipeline(**pipeline_config, training=train_triples_factory, testing=test_triples_factory, validation=val_triples_factory)

# Print the evaluation results
print("Evaluation results:")
for metric, value in results['test'].items():
    print(f"{metric}: {value:.4f}")
